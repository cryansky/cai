"""
These are tools for interacting with Confluence Cloud via the v2 REST API.
"""

import os
import re
import requests
import difflib
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

def _fuzzy_find_excerpt(page_body: str, excerpt: str, cutoff: float = 0.95) -> str | None:
    # Normalize whitespace and case
    norm_page = re.sub(r'\s+', ' ', page_body).strip().lower()
    norm_excerpt = re.sub(r'\s+', ' ', excerpt).strip().lower()

    # Generate larger sliding windows around the size of the excerpt
    window_size = len(norm_excerpt) + 20
    candidates = [
        norm_page[i:i + window_size]
        for i in range(0, len(norm_page) - window_size, max(10, window_size // 10))
    ]

    # Find best match
    matches = difflib.get_close_matches(norm_excerpt, candidates, n=1, cutoff=cutoff)
    return matches[0] if matches else None

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

def read_confluence_page(page_id: str) -> str:
    """
    Retrieves the plain text content of a Confluence page using its page ID.

    Args:
        page_id (str): The unique ID of the Confluence page.

    Returns:
        str: Cleaned page content (plain text) or an error message.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        page_detail_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
        response = requests.get(page_detail_url, headers=headers, auth=auth)
        response.raise_for_status()

        page_body = response.json()["body"]["storage"]["value"]
        page_body = _remove_confluence_namespaced_tags(page_body)
        page_body = _strip_html_to_text(page_body)

        soup = BeautifulSoup(page_body, 'html.parser')
        return soup.get_text()

    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e} — {e.response.text}"
    except Exception as e:
        return f"Error reading Confluence page: {e}"

def write_confluence_inline_comment(page_id: str, excerpt: str, comment: str) -> str:
    """
    Adds an inline comment to a Confluence page.

    Args:
        page_id (str): The unique ID of the Confluence page.
        excerpt (str): The exact string (including the HTML tags) on the page to anchor the comment to. This match must be case-sensitive and character-exact.
        comment (str): The comment content to post.

    Returns:
        str: Result message or error.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        page_detail_url = f"{CONFLUENCE_URL}/wiki/api/v2/pages/{page_id}?body-format=storage"
        response = requests.get(page_detail_url, headers=headers, auth=auth)
        response.raise_for_status()

        page_body = response.json()["body"]["storage"]["value"]
        page_body = _remove_confluence_namespaced_tags(page_body)
        page_body = _strip_html_to_text(page_body)

        soup = BeautifulSoup(page_body, 'html.parser')        
        page_body = soup.get_text()

        match = _fuzzy_find_excerpt(page_body, excerpt) # page_body.find(excerpt)
        print("Match", match)

        if not match:
            return "Excerpt not found in page content. Cannot create inline comment."

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
                "textSelectionMatchCount": 1,
                "textSelectionMatchIndex": 0
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
    
def read_confluence_inline_comments(page_id: str) -> list:
    """
    Retrieve all inline comments associated with a specific Confluence page.

    Args:
        page_id (str): The unique ID of the Confluence page.

    Returns:
        list: A list of inline comment objects and the excerpt the comment attached to.
    """
    if not auth:
        raise ValueError("Confluence credentials are missing or invalid.")

    try:
        url = f"{CONFLUENCE_URL}/wiki/api/v2/inline-comments"
        params = {
            "id": page_id, 
            "body-format": "storage"
        }

        response = requests.get(url, headers=headers, auth=auth, params=params)
        response.raise_for_status()

        comments = []
        for c in response.json().get("results", []):
            excerpt = c.get('properties', {}).get('inlineOriginalSelection')
            comment = c.get('body', {}).get('storage', {}).get('value')
            if excerpt and comment:
                comments.append({
                    "Excerpt": excerpt,
                    "Comment": comment
                })
        return comments
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