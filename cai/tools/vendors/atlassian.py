"""
These are tools for interacting with Confluence Cloud via the v2 REST API.
"""

import os
import re
import requests
from requests.auth import HTTPBasicAuth
import html
import json
from bs4 import BeautifulSoup

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL") 
CONFLUENCE_USER = os.getenv("CONFLUENCE_USER")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

if all([CONFLUENCE_URL, CONFLUENCE_USER, CONFLUENCE_API_TOKEN]):
    auth = HTTPBasicAuth(CONFLUENCE_USER, CONFLUENCE_API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
else:
    auth = None
    headers = {}

def _strip_html_to_text(text):
    # Remove all HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities (e.g., &rsquo; -> ’)
    text = html.unescape(text)

    return text

def _remove_confluence_namespaced_tags(text):
    # Remove all self-closing namespaced tags like <ac:tag/>
    text = re.sub(r'<[a-z]+:[^>/]+?/>', '', text)
    # Remove all opening namespaced tags like <ac:tag ...>
    text = re.sub(r'<[a-z]+:[^>]+?>', '', text)
    # Remove all closing namespaced tags like </ac:tag>
    text = re.sub(r'</[a-z]+:[^>]+?>', '', text)

    return text

def read_confluence_page(space: str, title: str) -> str:
    """
    Retrieves the HTML content of a Confluence page.

    Args:
        space (str): Space key (e.g., 'ENG' or '~userId' for personal spaces).
        title (str): Exact title of the page.

    Returns:
        str: Page content (HTML) or an error message.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        page_search_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages"
        params = {
            "spaceKey": space,
            "title": title,
            "limit": 1
        }

        response = requests.get(page_search_url, headers=headers, auth=auth, params=params)
        response.raise_for_status()
        results = response.json().get("results", [])

        if not results:
            return f"Page titled '{title}' not found in space '{space}'."

        page_id = results[0]["id"]

        page_detail_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
        detail_response = requests.get(page_detail_url, headers=headers, auth=auth)
        detail_response.raise_for_status()

        page_body = detail_response.json()["body"]["storage"]["value"]
        page_body = _remove_confluence_namespaced_tags(page_body)
        page_body = _strip_html_to_text(page_body)
        soup = BeautifulSoup(page_body, 'html.parser')

        return soup.get_text()

    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e} — {e.response.text}"
    except Exception as e:
        return f"Error reading Confluence page: {e}"

def write_confluence_inline_comment(space: str, title: str, excerpt: str, comment: str) -> str:
    """
    Adds an inline comment to a Confluence page.

    Args:
        space (str): Space key where the page is located.
        title (str): Title of the Confluence page.
        excerpt (str): The exact string (including the HTML tags) on the page to anchor the comment to. This match must be case-sensitive and character-exact.
        comment (str): The comment content to post.

    Returns:
        str: Result message or error.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        page_search_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages"
        params = {
            "spaceKey": space,
            "title": title,
            "limit": 1
        }
        response = requests.get(page_search_url, headers=headers, auth=auth, params=params)
        response.raise_for_status()
        results = response.json().get("results", [])
        if not results:
            return f"Page titled '{title}' not found in space '{space}'."

        page_id = results[0]["id"]

        page_detail_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
        detail_resp = requests.get(page_detail_url, headers=headers, auth=auth)
        detail_resp.raise_for_status()

        page_body = detail_resp.json()["body"]["storage"]["value"]
        page_body = _remove_confluence_namespaced_tags(page_body)
        page_body = _strip_html_to_text(page_body)

        soup = BeautifulSoup(page_body, 'html.parser')        
        page_body = soup.get_text()

        match_index = page_body.find(excerpt)

        if match_index == -1:
            return "Excerpt not found in page content. Cannot create inline comment."

        match_count = page_body.count(excerpt)
        match_index = match_count - 1
        excerpt = _strip_html_to_text(excerpt)
        
        comment_url = f"{CONFLUENCE_URL}/wiki/api/v2/inline-comments"
        payload = {
            "pageId": page_id,
            "body": {
                "representation": "storage",
                "value": f"<p>{html.escape(comment)}</p>"
            },
            "inlineCommentProperties": {
                "textSelection": excerpt,
                "textSelectionMatchCount": match_count,
                "textSelectionMatchIndex": match_index
            }
        }

        post_resp = requests.post(comment_url, headers=headers, auth=auth, data=json.dumps(payload))
        post_resp.raise_for_status()
        comment_id = post_resp.json().get("id", "unknown")
        
        return f"Inline comment posted successfully (ID: {comment_id})"

    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e} — {e.response.text}"
    except Exception as e:
        return f"Error posting inline comment: {e}"
    
def read_confluence_inline_comments() -> list:
    """
    Fetch all inline comments.

    Returns:
        list: A list of inline comment objects.
    """
    if not auth:
        raise ValueError("Confluence credentials are missing or invalid.")

    try:
        url = f"{CONFLUENCE_URL}/wiki/api/v2/inline-comments"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching inline comments: {e}")
        return []

def reply_to_confluence_comment(comment_id: str, reply_text: str) -> str:
    """
    Post a reply to a specific Confluence comment.

    Args:
        comment_id (str): The ID of the parent comment to reply to.
        reply_text (str): The content of the reply.

    Returns:
        str: Success message or error description.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        url = f"{CONFLUENCE_URL}/wiki/api/v2/comments"
        payload = {
            "parentId": comment_id,
            "body": {
                "representation": "storage",
                "value": f"<p>{html.escape(reply_text)}</p>"
            }
        }
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        comment_id = response.json().get("id", "unknown")
        return f"Reply posted successfully (ID: {comment_id})"
    except requests.exceptions.RequestException as e:
        return f"Error posting reply: {e}"