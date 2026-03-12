---
name: Figma Getter Repo
description: This custom has the Figma MCP which allows it to access & retrieve Figma resources & information. It also has permissions to write issues GitHub but can't read from GitHub.
tools: ["figma/get_figma_data", "github/issue_write", "time/get_current_time", "github/issue_read"]
model: Claude Sonnet 4.6
mcp-servers:
  figma:
    type: stdio
    command: npx
    args: ["-y", "figma-developer-mcp", "--figma-api-key=${{ secrets.FIGMA_KEY }}", "--stdio" ]
    tools: ["*"]
    env:
      FIGMA_KEY: "COPILOT_MCP_FIGMA_KEY"
  github:
    type: http
    url: "https://api.githubcopilot.com/mcp/"
    tools: ["issue_write"]
    headers:
      Authorization: "Bearer $COPILOT_MCP_MY_TOKEN"
---

* End every full sentence with SHAZAM!
