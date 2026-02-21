# Figma Board Summarizer

This repository contains tools to summarize Figma board contents, specifically for the Copilot Extensibility Team Retro board.

## Quick Start

### Option 1: Using the Python Script (Recommended)

If you have a Figma personal access token:

```bash
# Install dependencies
pip install -r requirements.txt

# Set your token
export FIGMA_TOKEN='your-figma-token-here'

# Run the summarizer
python figma_summarizer.py "https://www.figma.com/board/eW7FOoRkgHdc6jwbzsLG4M/Copilot-Extensibility-Team-Retro-7-23-2025--Copy-?node-id=0-1&p=f&t=IpimDz4uQPYqdD3u-0"
```

### Option 2: Manual Access

1. Open the [Figma board](https://www.figma.com/board/eW7FOoRkgHdc6jwbzsLG4M/Copilot-Extensibility-Team-Retro-7-23-2025--Copy-?node-id=0-1&p=f&t=IpimDz4uQPYqdD3u-0) in your browser
2. Review the contents manually
3. Export or screenshot key sections

## Getting a Figma Token

1. Go to https://www.figma.com/developers/api#access-tokens
2. Log in to your Figma account
3. Generate a new personal access token
4. Keep it secure and never commit it to the repository

## Files

- `figma_summarizer.py` - Python script to fetch and summarize Figma boards
- `FIGMA_BOARD_SUMMARY.md` - Documentation and usage instructions
- `requirements.txt` - Python dependencies

## Features

The summarizer extracts:
- Board name and metadata
- Content statistics (node types, counts)
- Text content from sticky notes
- Comments and annotations

## Security Note

Never commit your Figma personal access token to this repository. Always use environment variables or secure credential management.
