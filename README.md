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
        "quay.io/maorfr/tangerine-mcp"
      ],
      "env": {
        "TANGERINE_TOKEN": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with the OpenShift token.
