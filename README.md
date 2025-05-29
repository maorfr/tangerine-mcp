# tangerine-mcp

MCP server for Tangerine (Convo AI assistant backend): https://github.com/RedHatInsights/tangerine-backend

## Running with Podman or Docker

You can run the tangerine-mcp server in a container using Podman or Docker. Make sure you have a valid OpenShift token:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "ai-assistant": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "TANGERINE_TOKEN",
        "-e", "MCP_TRANSPORT",
        "quay.io/maorfr/tangerine-mcp:latest"
      ],
      "env": {
        "TANGERINE_TOKEN": "REDACTED",
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

Replace `REDACTED` with the OpenShift token.
