#!/usr/bin/env python3
"""
Figma Board Content Retriever

This script retrieves and summarizes content from a Figma board using the Figma REST API.
Requires a Figma personal access token for authentication.
"""

import os
import sys
import json
import requests
from typing import Dict, List, Any


def get_figma_file(file_id: str, token: str) -> Dict[str, Any]:
    """
    Retrieve a Figma file/board using the Figma API.
    
    Args:
        file_id: The Figma file ID (from the URL)
        token: Figma personal access token
        
    Returns:
        Dict containing the file data
    """
    url = f"https://api.figma.com/v1/files/{file_id}"
    headers = {
        "X-Figma-Token": token
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()


def extract_text_nodes(node: Dict[str, Any], texts: List[str]) -> None:
    """
    Recursively extract text content from Figma nodes.
    
    Args:
        node: A Figma node object
        texts: List to accumulate text content
    """
    if node.get("type") == "TEXT":
        text_content = node.get("characters", "")
        if text_content:
            texts.append(text_content)
    
    # Recursively process children
    children = node.get("children", [])
    for child in children:
        extract_text_nodes(child, texts)


def summarize_figma_board(file_id: str, token: str) -> str:
    """
    Retrieve and summarize a Figma board.
    
    Args:
        file_id: The Figma file ID
        token: Figma personal access token
        
    Returns:
        A formatted summary of the board content
    """
    try:
        data = get_figma_file(file_id, token)
        
        # Extract basic information
        file_name = data.get("name", "Unknown")
        last_modified = data.get("lastModified", "Unknown")
        
        # Extract all text content
        texts = []
        document = data.get("document", {})
        extract_text_nodes(document, texts)
        
        # Build summary
        summary = f"""# Figma Board Summary

## File Information
- **Name**: {file_name}
- **Last Modified**: {last_modified}
- **File ID**: {file_id}

## Content

Total text elements found: {len(texts)}

### Text Content:
"""
        
        for i, text in enumerate(texts, 1):
            # Truncate very long text
            display_text = text if len(text) <= 200 else text[:200] + "..."
            summary += f"\n{i}. {display_text}\n"
        
        return summary
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            return "Error: Access forbidden. Please check your Figma token and permissions."
        elif e.response.status_code == 404:
            return "Error: File not found. Please check the file ID."
        else:
            return f"Error: HTTP {e.response.status_code} - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main entry point for the script."""
    # Board ID from the problem statement
    file_id = "eW7FOoRkgHdc6jwbzsLG4M"
    
    # Get token from environment variable
    token = os.environ.get("FIGMA_TOKEN")
    
    if not token:
        print("Error: FIGMA_TOKEN environment variable not set.", file=sys.stderr)
        print("\nUsage:", file=sys.stderr)
        print("  export FIGMA_TOKEN='your_token_here'", file=sys.stderr)
        print("  python figma_board_retriever.py", file=sys.stderr)
        print("\nGet a personal access token from:", file=sys.stderr)
        print("  https://www.figma.com/developers/api#access-tokens", file=sys.stderr)
        sys.exit(1)
    
    print("Retrieving Figma board content...")
    summary = summarize_figma_board(file_id, token)
    print(summary)
    
    # Optionally save to file
    output_file = "figma_board_content.md"
    with open(output_file, "w") as f:
        f.write(summary)
    print(f"\nSummary saved to: {output_file}")


if __name__ == "__main__":
    main()
