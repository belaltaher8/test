#!/usr/bin/env python3
"""
Figma Board Content Retriever

This script retrieves content from a Figma board using the Figma REST API.
It requires a personal access token from Figma.

Usage:
    python figma_retriever.py <figma_file_id> <access_token>

To get a personal access token:
    1. Go to Figma Settings → Account → Personal Access Tokens
    2. Generate a new token
    3. Use it with this script

Example:
    python figma_retriever.py eW7FOoRkgHdc6jwbzsLG4M your-token-here
"""

import sys
import json
import requests
from typing import Dict, List, Any


def fetch_figma_file(file_id: str, access_token: str) -> Dict[str, Any]:
    """
    Fetch Figma file data using the REST API.
    
    Args:
        file_id: The Figma file ID (from the URL)
        access_token: Personal access token for authentication
        
    Returns:
        Dictionary containing the file data
    """
    url = f"https://api.figma.com/v1/files/{file_id}"
    headers = {
        "X-Figma-Token": access_token
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()


def extract_text_nodes(node: Dict[str, Any], texts: List[str] = None) -> List[str]:
    """
    Recursively extract all text content from Figma nodes.
    
    Args:
        node: A Figma node dictionary
        texts: List to accumulate text content
        
    Returns:
        List of text strings found in the node tree
    """
    if texts is None:
        texts = []
    
    # Check if this node has text content
    if node.get("type") == "TEXT" and "characters" in node:
        texts.append(node["characters"])
    
    # Check for sticky notes or other text-containing elements
    if "name" in node and node.get("characters"):
        texts.append(f"{node['name']}: {node['characters']}")
    
    # Recursively process children
    if "children" in node:
        for child in node["children"]:
            extract_text_nodes(child, texts)
    
    return texts


def format_retro_content(data: Dict[str, Any]) -> str:
    """
    Format the Figma data into a readable retro summary.
    
    Args:
        data: The Figma file data
        
    Returns:
        Formatted markdown string
    """
    output = []
    output.append("# Copilot Extensibility Team Retro - July 23, 2025\n")
    output.append(f"## File: {data.get('name', 'Unknown')}\n")
    
    # Extract all text content
    document = data.get("document", {})
    texts = extract_text_nodes(document)
    
    if texts:
        output.append("## Content\n")
        for i, text in enumerate(texts, 1):
            output.append(f"{i}. {text}\n")
    else:
        output.append("No text content found in the board.\n")
    
    return "\n".join(output)


def main():
    if len(sys.argv) < 3:
        print("Usage: python figma_retriever.py <file_id> <access_token>")
        print("\nFile ID: eW7FOoRkgHdc6jwbzsLG4M (from the URL)")
        print("Access Token: Get from Figma Settings → Personal Access Tokens")
        sys.exit(1)
    
    file_id = sys.argv[1]
    access_token = sys.argv[2]
    
    print(f"Fetching Figma file {file_id}...")
    
    try:
        data = fetch_figma_file(file_id, access_token)
        
        # Save raw data for debugging
        with open("figma_raw_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Raw data saved to figma_raw_data.json")
        
        # Format and save the summary
        summary = format_retro_content(data)
        with open("RETRO_NOTES_2025-07-23.md", "w") as f:
            f.write(summary)
        print("Summary saved to RETRO_NOTES_2025-07-23.md")
        
        print("\nPreview:")
        print(summary[:500] + "..." if len(summary) > 500 else summary)
        
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching from Figma API: {e}")
        print("Please check your file ID and access token.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
