"""
fs_tools.py - File system tools for resume analysis

This module has four main functions that can be used as LLM tools:
- read_file: reads PDF, TXT, DOCX files
- list_files: lists files in a directory  
- write_file: writes content to a file
- search_in_file: searches for keywords in files

Each function returns a dict with success/error info so the LLM
can understand what happened.
"""

import os
import datetime
from typing import Optional


# --- helpers to read different file types ---

def _read_txt(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def _read_pdf(filepath):
    # using PyPDF2 for pdf extraction
    from PyPDF2 import PdfReader
    reader = PdfReader(filepath)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)


def _read_docx(filepath):
    from docx import Document
    doc = Document(filepath)
    return "\n".join(p.text for p in doc.paragraphs)


# maps extension to the right reader function
_READERS = {
    ".txt": _read_txt,
    ".pdf": _read_pdf,
    ".docx": _read_docx,
}


def read_file(filepath: str) -> dict:
    """
    Reads a resume file and returns its text content + metadata.
    Supports .pdf, .txt and .docx formats.
    """
    try:
        filepath = os.path.abspath(filepath)

        if not os.path.isfile(filepath):
            return {"success": False, "content": None, "metadata": None,
                    "error": f"File not found: {filepath}"}

        ext = os.path.splitext(filepath)[1].lower()
        reader = _READERS.get(ext)
        if reader is None:
            return {"success": False, "content": None, "metadata": None,
                    "error": f"Unsupported format: {ext}. We support: {', '.join(_READERS)}"}

        content = reader(filepath)
        stat = os.stat(filepath)

        metadata = {
            "filename": os.path.basename(filepath),
            "size_bytes": stat.st_size,
            "extension": ext,
            "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
        }

        return {"success": True, "content": content, "metadata": metadata, "error": None}

    except Exception as e:
        return {"success": False, "content": None, "metadata": None, "error": str(e)}


def list_files(directory: str, extension: Optional[str] = None) -> dict:
    """
    Lists files in a directory. You can optionally filter by extension
    like ".pdf" or ".txt". Returns file metadata for each match.
    """
    try:
        directory = os.path.abspath(directory)

        if not os.path.isdir(directory):
            return {"success": False, "files": [], "total": 0,
                    "error": f"Directory not found: {directory}"}

        # make sure extension has a dot
        if extension and not extension.startswith("."):
            extension = "." + extension

        results = []
        for entry in sorted(os.listdir(directory)):
            full_path = os.path.join(directory, entry)

            # skip directories, we only want files
            if not os.path.isfile(full_path):
                continue

            # apply extension filter if given
            if extension and not entry.lower().endswith(extension.lower()):
                continue

            stat = os.stat(full_path)
            results.append({
                "name": entry,
                "path": full_path,
                "size_bytes": stat.st_size,
                "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
            })

        return {"success": True, "files": results, "total": len(results), "error": None}

    except Exception as e:
        return {"success": False, "files": [], "total": 0, "error": str(e)}


def write_file(filepath: str, content: str) -> dict:
    """
    Writes text content to a file. Creates parent directories 
    if they don't exist yet.
    """
    try:
        filepath = os.path.abspath(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            written = f.write(content)

        return {"success": True, "filepath": filepath, "bytes_written": written, "error": None}

    except Exception as e:
        return {"success": False, "filepath": None, "bytes_written": None, "error": str(e)}


def search_in_file(filepath: str, keyword: str) -> dict:
    """
    Does a case-insensitive search for a keyword in a file.
    Returns matching lines with some surrounding context (1 line above and below).
    """
    try:
        # reuse our read_file function to get the text
        result = read_file(filepath)
        if not result["success"]:
            return {"success": False, "keyword": keyword, "matches": [],
                    "total_matches": 0, "error": result["error"]}

        lines = result["content"].splitlines()
        keyword_lower = keyword.lower()
        matches = []

        for i, line in enumerate(lines):
            if keyword_lower in line.lower():
                # grab 1 line before and after for context
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                context = "\n".join(lines[start:end])

                matches.append({
                    "line_number": i + 1,
                    "line": line.strip(),
                    "context": context,
                })

        return {
            "success": True,
            "keyword": keyword,
            "matches": matches,
            "total_matches": len(matches),
            "error": None,
        }

    except Exception as e:
        return {"success": False, "keyword": keyword, "matches": [],
                "total_matches": 0, "error": str(e)}


# Tool schema for Gemini function calling
# Each tool needs a name, description, and parameter definitions

TOOLS_SCHEMA = [
    {
        "name": "read_file",
        "description": "Read a resume file (PDF, TXT, or DOCX) and extract its text content along with file metadata.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "Path to the file to read.",
                }
            },
            "required": ["filepath"],
        },
    },
    {
        "name": "list_files",
        "description": "List all files in a directory, optionally filtered by extension (e.g. '.pdf'). Returns name, path, size, and modified date for each file.",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Path to the directory to list.",
                },
                "extension": {
                    "type": "string",
                    "description": "Optional extension filter like '.pdf' or '.txt'. Include the dot.",
                },
            },
            "required": ["directory"],
        },
    },
    {
        "name": "write_file",
        "description": "Write text content to a file. Creates parent directories if needed.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "Destination file path.",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write.",
                },
            },
            "required": ["filepath", "content"],
        },
    },
    {
        "name": "search_in_file",
        "description": "Search for a keyword in a file (case-insensitive). Returns matching lines with surrounding context.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {
                    "type": "string",
                    "description": "Path to the file to search.",
                },
                "keyword": {
                    "type": "string",
                    "description": "Keyword or phrase to search for.",
                },
            },
            "required": ["filepath", "keyword"],
        },
    },
]

# quick lookup: function name -> actual function
TOOL_DISPATCH = {
    "read_file": read_file,
    "list_files": list_files,
    "write_file": write_file,
    "search_in_file": search_in_file,
}


# quick test - run this file directly to see if everything works
if __name__ == "__main__":
    import json

    print("=== Testing list_files ===")
    print(json.dumps(list_files("resumes"), indent=2))

    print("\n=== Testing read_file ===")
    res = read_file("resumes/resume_arjun_sharma.txt")
    print(json.dumps(res, indent=2))

    print("\n=== Testing search_in_file ===")
    print(json.dumps(search_in_file("resumes/resume_arjun_sharma.txt", "python"), indent=2))

    print("\n=== Testing write_file ===")
    print(json.dumps(write_file("output/test.txt", "Hello World"), indent=2))
