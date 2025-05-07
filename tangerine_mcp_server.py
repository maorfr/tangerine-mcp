import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("tangerine")

TANGERINE_API_BASE = "https://tangerine.devshift.net/api/assistants/{assistant_id}/chat"


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


async def query_assistant(
    assistant_id: int, query_text: str, interaction_id: str
) -> str:
    query_url = TANGERINE_API_BASE.format(assistant_id=assistant_id)
    return await make_request(query_url, query_text, interaction_id)


@mcp.tool()
async def query_clowder_assistant(query_text: str, interaction_id: str) -> str:
    """Query the clowder assistant (ID: 1)."""
    return await query_assistant(1, query_text, interaction_id)


@mcp.tool()
async def query_consoledot_pages_assistant(query_text: str, interaction_id: str) -> str:
    """Query the consoledot-pages assistant (ID: 3)."""
    return await query_assistant(3, query_text, interaction_id)


@mcp.tool()
async def query_firelink_assistant(query_text: str, interaction_id: str) -> str:
    """Query the firelink assistant (ID: 4)."""
    return await query_assistant(4, query_text, interaction_id)


@mcp.tool()
async def query_hccm_assistant(query_text: str, interaction_id: str) -> str:
    """Query the hccm assistant (ID: 5)."""
    return await query_assistant(5, query_text, interaction_id)


@mcp.tool()
async def query_notifications_assistant(query_text: str, interaction_id: str) -> str:
    """Query the notifications assistant (ID: 6)."""
    return await query_assistant(6, query_text, interaction_id)


@mcp.tool()
async def query_yuptoo_assistant(query_text: str, interaction_id: str) -> str:
    """Query the yuptoo assistant (ID: 7)."""
    return await query_assistant(7, query_text, interaction_id)


@mcp.tool()
async def query_inscope_all_docs_agent_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the inscope-all-docs-agent assistant (ID: 8)."""
    return await query_assistant(8, query_text, interaction_id)


@mcp.tool()
async def query_inscope_onboarding_guide_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the inscope-onboarding-guide assistant (ID: 10)."""
    return await query_assistant(10, query_text, interaction_id)


@mcp.tool()
async def query_frontend_experience_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the frontend-experience assistant (ID: 11)."""
    return await query_assistant(11, query_text, interaction_id)


@mcp.tool()
async def query_incident_management_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the incident-management assistant (ID: 12)."""
    return await query_assistant(12, query_text, interaction_id)


@mcp.tool()
async def query_roms_onboarding_guide_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the roms-onboarding-guide assistant (ID: 13)."""
    return await query_assistant(13, query_text, interaction_id)


@mcp.tool()
async def query_managed_openshift_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the managed-openshift assistant (ID: 15)."""
    return await query_assistant(15, query_text, interaction_id)


@mcp.tool()
async def query_openshift_ci_assistant(query_text: str, interaction_id: str) -> str:
    """Query the openshift-ci assistant (ID: 16)."""
    return await query_assistant(16, query_text, interaction_id)


@mcp.tool()
async def query_app_sre_app_interface_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the app-sre-app-interface assistant (ID: 17)."""
    return await query_assistant(17, query_text, interaction_id)


@mcp.tool()
async def query_app_sre_dev_guidelines_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the app-sre-dev-guidelines assistant (ID: 18)."""
    return await query_assistant(18, query_text, interaction_id)


@mcp.tool()
async def query_app_sre_contract_assistant(query_text: str, interaction_id: str) -> str:
    """Query the app-sre-contract assistant (ID: 19)."""
    return await query_assistant(19, query_text, interaction_id)


@mcp.tool()
async def query_konflux_assistant(query_text: str, interaction_id: str) -> str:
    """Query the konflux assistant (ID: 21)."""
    return await query_assistant(21, query_text, interaction_id)


@mcp.tool()
async def query_ocm_clusters_service_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the ocm-clusters-service assistant (ID: 22)."""
    return await query_assistant(22, query_text, interaction_id)


@mcp.tool()
async def query_hcm_architecture_documents_assistant(
    query_text: str, interaction_id: str
) -> str:
    """Query the HCM architecture documents assistant (ID: 23)."""
    return await query_assistant(23, query_text, interaction_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
