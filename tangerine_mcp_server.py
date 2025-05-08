import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("tangerine")

TANGERINE_API_BASE = "https://tangerine.devshift.net/api/assistants/{assistant_id}/search"


async def make_request(
    url: str, query_text: str, interaction_id: str
) -> dict[str, Any] | None:
    token = os.environ["TANGERINE_TOKEN"]

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {
        "client": "curl",
        "interactionId": interaction_id,
        "prevMsgs": [],
        "query": query_text,
        "stream": "false",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=30.0)
            response.raise_for_status()
            return response.json()["text_content"]
        except Exception as e:
            print(e)
            return None


async def query(assistant_id: int, query_text: str, interaction_id: str) -> str:
    query_url = TANGERINE_API_BASE.format(assistant_id=assistant_id)
    return await make_request(query_url, query_text, interaction_id)


@mcp.tool()
async def managed_openshift(query_text: str, interaction_id: str) -> str:
    """Query the managed-openshift assistant (ID: 15)."""
    return await query(15, query_text, interaction_id)


@mcp.tool()
async def app_interface(query_text: str, interaction_id: str) -> str:
    """Query the app-sre-app-interface assistant (ID: 17)."""
    return await query(17, query_text, interaction_id)


@mcp.tool()
async def konflux(query_text: str, interaction_id: str) -> str:
    """Query the konflux assistant (ID: 21)."""
    return await query(21, query_text, interaction_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
