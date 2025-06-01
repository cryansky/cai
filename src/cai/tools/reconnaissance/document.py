"""
These are the tools for the model to read and write to files and other documents.
"""

import pymupdf

def read_pdf_content(pdf_path: str) -> str:
    """
    Extracts and concatenates text content from all pages of a PDF file.

    Args:
        pdf_path (str): Absolute or relative path to the target PDF file.

    Returns:
        str: 
            - On success: A newline-separated string of extracted text from each page that contains text.
            - On failure: A string describing the error encountered during reading or parsing.

    Notes:
        - Pages with no extractable text (e.g., image-only content) are skipped.
        - If an exception occurs (e.g., file not found, corrupted file), the exception message is returned as a string.
        - Designed to support downstream LLM tasks like summarization, question answering, or comment generation.

    Example:
        text = extract_text_from_pdf("sample.pdf")
    """
    try:
        doc = pymupdf.open(pdf_path)
        return "\n".join(page.get_text() for page in doc if page.get_text())
    except Exception as e:
        return f"Error reading PDF: {e}"

def add_comment_to_pdf(pdf_path: str, output_path: str, excerpt: str, comment: str):
    """
    Search for a text excerpt in a PDF and add a comment annotation at each match.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path where the annotated PDF will be saved.
        excerpt (str): The exact text string to search for in the document.
        comment (str): The text of the comment to attach as an annotation.

    Returns:
        dict: A dictionary with:
            - "success" (bool): True if any annotations were added, False otherwise.
            - "output_path" (str): The path to the saved annotated PDF.
    """

    doc = pymupdf.open(pdf_path)
    found = False

    for page in doc:
        matches = page.search_for(excerpt)
        if matches:
            highlight = page.add_highlight_annot(matches)
            highlight.set_info(info={"content": comment})
            found = True

    doc.save(output_path, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    return {"success": found, "output_path": output_path}

