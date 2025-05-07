# ocm-mcp

MCP server for Tangerine (Convo AI assistant backend)

## Running with Podman or Docker

You can run the tangerine-mcp server in a container using Podman or Docker. Make sure you have a valid OpenShift token:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "tangerine-mcp": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "OC_TOKEN",
        "quay.io/maorfr/tangerine-mcp"
      ],
      "env": {
        "OC_TOKEN": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with the OpenShift token.
