"""
These are tools for interacting with Confluence Cloud via the v2 REST API.
"""

import os
import re
import requests
from requests.auth import HTTPBasicAuth
import html
import json
import html2text
from langchain_community.document_loaders import ConfluenceLoader
from cai.sdk.agents import function_tool

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL") 
CONFLUENCE_USER = os.getenv("CONFLUENCE_USER")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
CONFLUENCE_SEARCH_SPACE = os.getenv("CONFLUENCE_SEARCH_SPACE")

if all([CONFLUENCE_URL, CONFLUENCE_USER, CONFLUENCE_API_TOKEN]):
    auth = HTTPBasicAuth(CONFLUENCE_USER, CONFLUENCE_API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
else:
    auth = None
    headers = {}

def _normalize_markdown(md_text: str) -> str:
    """
    Strips common Markdown syntax and returns plain visible text.
    """
    # Remove inline code and bold/italic markers
    text = re.sub(r'`([^`]*)`', r'\1', md_text)        # `code`
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)     # **bold**
    text = re.sub(r'\*([^*]+)\*', r'\1', text)         # *italic*
    text = re.sub(r'__([^_]+)__', r'\1', text)         # __bold__
    text = re.sub(r'_([^_]+)_', r'\1', text)           # _italic_
    text = re.sub(r'\s+', ' ', text)                   # normalize all whitespaces

    # Remove headings
    text = re.sub(r'^#{1,6}\s*', '', text, flags=re.MULTILINE)
    # Remove blockquotes
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove link syntax but keep visible text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # [text](url)
    # Remove image syntax: ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    # Remove list bullets and numbers
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^-{3,}|^\*{3,}', '', text, flags=re.MULTILINE)

    # Strip remaining markdown artifacts
    return text.strip()

def _remove_confluence_namespaced_tags(text):
    # Remove all self-closing namespaced tags like <ac:tag/>
    text = re.sub(r'<[a-z]+:[^>/]+?/>', '', text)
    # Remove all opening namespaced tags like <ac:tag ...>
    text = re.sub(r'<[a-z]+:[^>]+?>', '', text)
    # Remove all closing namespaced tags like </ac:tag>
    text = re.sub(r'</[a-z]+:[^>]+?>', '', text)

    return text

@function_tool
def search_confluence(query: str, search_space: str = CONFLUENCE_SEARCH_SPACE, max_pages: int = 5):
    """
    Search Confluence pages based on search keywords or phrase.

    Args:
        query (str): Search keywords or phrase.
        search_space (str): Space key to search.
        max_pages (int): Maximum number of pages to return.

    Returns:
        list: List of dicts {title, url, text}
    """
    if not all([CONFLUENCE_URL, CONFLUENCE_USER, CONFLUENCE_API_TOKEN]):
        return [{"error": "Confluence credentials missing"}]
    
    cql = (
        f'(type = "page" OR type = "blogpost") '
        + (f'AND space = "{search_space}" ' if search_space else '')
        + f'AND (title ~ "{query}" OR text ~ "{query}") '
        'ORDER BY lastmodified DESC'
    )
    
    loader = ConfluenceLoader(
        url=CONFLUENCE_URL,
        username=CONFLUENCE_USER,
        api_key=CONFLUENCE_API_TOKEN,
        cql=cql,
        max_pages=max_pages,
        include_attachments=False,
        keep_markdown_format=True
    )

    try:
        docs = loader.load()
        results = []
        for doc in docs:
            content = doc.page_content
            metadata = doc.metadata
            results.append({
                "title": metadata.get("title", ""),
                "url": metadata.get("source", ""),
                "text": content
            })
        if results:
            return results
        else:
            return "No document found. Try supplying a more generalized query."
    except Exception as e:
        return [{"error": str(e)}]

def _read_confluence_page(page_id: str) -> str:
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
        loader = ConfluenceLoader(
            url=CONFLUENCE_URL,
            username=CONFLUENCE_USER,
            api_key=CONFLUENCE_API_TOKEN,
            page_ids=[page_id],
            keep_markdown_format=True,
            max_pages=1
        )
        docs = loader.load()
        if docs:
            content = docs[0].page_content
            return content
        else:
            return "Page not found."
    except requests.exceptions.HTTPError as e:
        return f"HTTP error: {e} — {e.response.text}"
    except Exception as e:
        return f"Error reading Confluence page: {e}"

@function_tool
def read_confluence_page(page_id: str) -> str:
    return _read_confluence_page(page_id)

@function_tool
def write_confluence_inline_comment(page_id: str, excerpt: str, comment: str) -> str:
    """
    Adds an inline comment to a Confluence page.

    Args:
        page_id (str): The unique ID of the Confluence page.
        excerpt (str): The exact string (without any tags or markdown elements) on the page to anchor the comment to. This match must be case-sensitive and character-exact.
        comment (str): The comment content to post.

    Returns:
        str: Result message or error.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        page_body = _read_confluence_page(page_id)

        page_body = _normalize_markdown(page_body)
        excerpt = _normalize_markdown(excerpt)

        n_match = page_body.count(excerpt)
        n_match = n_match if n_match else 1
        
        comment_url = f"{CONFLUENCE_URL}/wiki/api/v2/inline-comments"
        for m in range(n_match):
            payload = {
                "pageId": page_id,
                "body": {
                    "representation": "storage",
                    "value": f"<p>{html.escape(comment)}</p>"
                },
                "inlineCommentProperties": {
                    "textSelection": excerpt,
                    "textSelectionMatchCount": n_match,
                    "textSelectionMatchIndex": m
                }
            }
            # print(json.dumps(payload))

        post_resp = requests.post(comment_url, headers=headers, auth=auth, data=json.dumps(payload))
        post_resp.raise_for_status()
        comment_id = post_resp.json().get("id", "unknown")

        return f"Inline comment posted successfully (ID: {comment_id})"

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            return f"HTTP error: {e} - Excerpt might not be found on the Confluence page or might contain invalid characters."
        return f"HTTP error: {e} — {e.response.text}"
    except Exception as e:
        return f"Error posting inline comment: {e}"

@function_tool    
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

@function_tool
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

@function_tool    
def write_confluence_footer_comment(page_id: str, comment_text: str, parent_comment_id: str = None) -> str:
    """
    Post a footer comment to a Confluence page.

    Footer comments are used only when inline comments cannot be inserted. They appear
    at the bottom of the page and can also be used to reply to an existing comment
    by specifying `parent_comment_id`.

    Args:
        page_id (str): The ID of the Confluence page to comment on.
        comment_text (str): The content of the comment.
        parent_comment_id (str, optional): ID of the comment to reply to (if replying).

    Returns:
        str: Success message or error description.
    """
    if not auth:
        return "Confluence credentials are missing or invalid."

    try:
        url = f"{CONFLUENCE_URL}/wiki/api/v2/footer-comments"
        payload = {
            "pageId": page_id,
            "body": {
                "representation": "storage",
                "value": f"<p>{html.escape(comment_text)}</p>"
            }
        }

        if parent_comment_id:
            payload["parentCommentId"] = parent_comment_id

        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()

        comment_id = response.json().get("id", "unknown")
        return f"Footer comment posted successfully (ID: {comment_id})"
    except requests.exceptions.RequestException as e:
        return f"Error posting footer comment: {e}"