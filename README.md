# Copilot Extensibility Team Retro Repository

This repository contains retrospective notes and tools for the Copilot Extensibility Team.

## Current Retro

**Date:** July 23, 2025  
**Figma Board:** [Copilot Extensibility Team Retro](https://www.figma.com/board/eW7FOoRkgHdc6jwbzsLG4M/Copilot-Extensibility-Team-Retro-7-23-2025--Copy-?node-id=0-1&p=f&t=IpimDz4uQPYqdD3u-0)

## Files

- `RETRO_NOTES_2025-07-23.md` - Template for retro notes (needs to be populated with Figma board content)
- `figma_retriever.py` - Python script to fetch content from Figma boards using the API

## How to Populate Retro Notes

### Option 1: Manual Update

1. Open the [Figma board](https://www.figma.com/board/eW7FOoRkgHdc6jwbzsLG4M/Copilot-Extensibility-Team-Retro-7-23-2025--Copy-?node-id=0-1&p=f&t=IpimDz4uQPYqdD3u-0) in your browser
2. Copy the content from sticky notes and sections
3. Edit `RETRO_NOTES_2025-07-23.md` and paste the content into appropriate sections

### Option 2: Using the Figma API Script

1. **Get a Figma Personal Access Token:**
   - Go to [Figma Settings](https://www.figma.com/settings)
   - Navigate to Account → Personal Access Tokens
   - Click "Generate new token"
   - Copy the token (you won't be able to see it again)

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Run the script:**
   ```bash
   python figma_retriever.py eW7FOoRkgHdc6jwbzsLG4M YOUR_ACCESS_TOKEN
   ```

4. **Review the output:**
   - The script will save `figma_raw_data.json` with the complete API response
   - The script will update `RETRO_NOTES_2025-07-23.md` with extracted content

### Option 3: Export from Figma

1. Open the Figma board
2. Use File → Export to export the board as images or PDF
3. Add the exported files to this repository
4. Reference them in the retro notes document

## Notes

- The Figma board is private and requires authentication to access
- The script uses the Figma REST API which requires a personal access token
- Never commit your personal access token to the repository
