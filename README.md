# Figma Board Summarizer

This repository contains tools to retrieve and summarize content from Figma boards.

## Overview

The target Figma board is:
- **URL**: https://www.figma.com/board/eW7FOoRkgHdc6jwbzsLG4M/Copilot-Extensibility-Team-Retro-7-23-2025--Copy-
- **Board ID**: `eW7FOoRkgHdc6jwbzsLG4M`
- **Title**: Copilot Extensibility Team Retro (7/23/2025)

## Files

- `FIGMA_BOARD_SUMMARY.md` - Documentation and information about the Figma board
- `figma_board_retriever.py` - Python script to retrieve and summarize Figma board content via API

## Prerequisites

To retrieve content from private Figma boards, you need:

1. **Figma Personal Access Token**
   - Generate one at: https://www.figma.com/developers/api#access-tokens
   - Requires appropriate permissions to access the board

2. **Python 3.x** with the `requests` library
   ```bash
   pip install requests
   ```

## Usage

### Option 1: Using the Python Script

1. Set your Figma token as an environment variable:
   ```bash
   export FIGMA_TOKEN='your_figma_personal_access_token'
   ```

2. Run the script:
   ```bash
   python figma_board_retriever.py
   ```

3. The summary will be displayed and saved to `figma_board_content.md`

### Option 2: Manual Access

If you have access to the Figma board:
1. Open the URL in a browser
2. Review the content manually
3. Update `FIGMA_BOARD_SUMMARY.md` with the findings

## Limitations

- Figma blocks automated web scraping via robots.txt
- Private boards require authentication
- API access requires a personal access token with appropriate permissions
- Direct web fetch attempts will fail

## Previous Successful Retrievals

According to repository history, this board has been successfully accessed using a FigmaGetter custom agent that retrieved:
- Ice breaker responses
- Positives (what went well)
- Challenges (what could be improved)
- Learnings/questions/concerns
- Action items

The board contains retrospective meeting notes from the Copilot Extensibility Team.

## Security Note

⚠️ **Never commit your Figma personal access token to the repository!**
- Always use environment variables
- Add `.env` files to `.gitignore` if using them
- Rotate tokens if accidentally exposed

## Learn More

- [Figma REST API Documentation](https://www.figma.com/developers/api)
- [Figma API Authentication](https://www.figma.com/developers/api#authentication)
