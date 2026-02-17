#!/usr/bin/env python3
"""
Figma Board Summarizer

This script provides functionality to summarize Figma board contents.
Requires a Figma personal access token to use the Figma REST API.
"""

import os
import sys
import json
from typing import Dict, Any, List

def get_figma_token() -> str:
    """Get Figma API token from environment variable."""
    token = os.environ.get('FIGMA_TOKEN')
    if not token:
        print("Error: FIGMA_TOKEN environment variable not set", file=sys.stderr)
        print("Get your token from: https://www.figma.com/developers/api#access-tokens", file=sys.stderr)
        sys.exit(1)
    return token

def extract_board_id(url: str) -> str:
    """Extract board/file ID from Figma URL."""
    # URL format: https://www.figma.com/board/{file_id}/...
    parts = url.split('/')
    for i, part in enumerate(parts):
        if part == 'board' and i + 1 < len(parts):
            return parts[i + 1]
    raise ValueError(f"Could not extract board ID from URL: {url}")

def fetch_figma_board(file_id: str, token: str) -> Dict[str, Any]:
    """
    Fetch Figma board data using the Figma REST API.
    
    Note: This requires the 'requests' library.
    Install with: pip install requests
    """
    try:
        import requests
    except ImportError:
        print("Error: requests library not installed", file=sys.stderr)
        print("Install with: pip install requests", file=sys.stderr)
        sys.exit(1)
    
    headers = {
        'X-Figma-Token': token
    }
    
    url = f'https://api.figma.com/v1/files/{file_id}'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: API returned status {response.status_code}", file=sys.stderr)
        print(f"Response: {response.text}", file=sys.stderr)
        sys.exit(1)
    
    return response.json()

def summarize_board(data: Dict[str, Any]) -> str:
    """Generate a text summary of the Figma board."""
    summary_parts = []
    
    # Board name
    board_name = data.get('name', 'Untitled Board')
    summary_parts.append(f"# {board_name}\n")
    
    # Document info
    last_modified = data.get('lastModified', 'Unknown')
    summary_parts.append(f"**Last Modified**: {last_modified}\n")
    
    # Count nodes
    document = data.get('document', {})
    def count_nodes(node: Dict[str, Any], node_types: Dict[str, int]):
        node_type = node.get('type', 'UNKNOWN')
        node_types[node_type] = node_types.get(node_type, 0) + 1
        for child in node.get('children', []):
            count_nodes(child, node_types)
    
    node_types = {}
    count_nodes(document, node_types)
    
    summary_parts.append("\n## Content Summary\n")
    for node_type, count in sorted(node_types.items()):
        summary_parts.append(f"- {node_type}: {count}\n")
    
    # Extract text content
    def extract_text(node: Dict[str, Any], texts: List[str]):
        if 'characters' in node:
            text = node['characters'].strip()
            if text:
                texts.append(text)
        for child in node.get('children', []):
            extract_text(child, texts)
    
    texts = []
    extract_text(document, texts)
    
    if texts:
        summary_parts.append(f"\n## Text Content ({len(texts)} items)\n")
        for i, text in enumerate(texts[:10], 1):  # Show first 10
            preview = text[:100] + '...' if len(text) > 100 else text
            summary_parts.append(f"{i}. {preview}\n")
        
        if len(texts) > 10:
            summary_parts.append(f"\n... and {len(texts) - 10} more items\n")
    
    return ''.join(summary_parts)

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python figma_summarizer.py <figma_board_url>")
        print("\nExample:")
        print("  export FIGMA_TOKEN='your-token-here'")
        print("  python figma_summarizer.py 'https://www.figma.com/board/...'")
        sys.exit(1)
    
    board_url = sys.argv[1]
    
    print("Extracting board ID from URL...")
    file_id = extract_board_id(board_url)
    print(f"Board ID: {file_id}")
    
    print("\nFetching Figma token...")
    token = get_figma_token()
    
    print("Fetching board data from Figma API...")
    data = fetch_figma_board(file_id, token)
    
    print("\nGenerating summary...\n")
    summary = summarize_board(data)
    print(summary)
    
    # Save to file
    output_file = 'figma_board_summary.md'
    with open(output_file, 'w') as f:
        f.write(summary)
    print(f"\nSummary saved to: {output_file}")

if __name__ == '__main__':
    main()
