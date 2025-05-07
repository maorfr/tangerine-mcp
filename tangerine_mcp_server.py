import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("tangerine")

TANGERINE_API_BASE = "https://tangerine.devshift.net/api/assistants/21/chat"

AI_ASSISTANT_PROMPT = """
You are a technical AI assistant designed to help developers debug build failures. You receive as input build logs containing error messages, warnings, and other diagnostic output from Konflux.

Your task is to:

1. Analyze the provided build logs to identify the root cause of the failure, including specific error messages, stack traces, and contextual information.

2. Explain in clear, developer-friendly language what the error means, what component or tool is involved, and why the failure likely occurred.

3. Suggest actionable next steps or fixes that the developer can try to resolve the problem.

4. If necessary, retrieve additional information from relevant documentation, error code descriptions, or troubleshooting guides to provide a more complete and accurate explanation.

When providing your answer:

- Clearly indicate the error(s) you identified.
- Offer concise and precise explanations.
- When appropriate, include example commands, config snippets, or code adjustments.
- If multiple issues are present, prioritize fatal errors or those most likely causing the build to fail.

Input:

{failure_text}

Output:

- Root cause(s) summary
- Explanation of the issue(s)
- Recommended fix(es) or next step(s)
- (Optional) Additional resources or references
"""


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


@mcp.tool()
async def query(failure_text: str, interaction_id: str) -> str:
    query_url = TANGERINE_API_BASE
    query_text = AI_ASSISTANT_PROMPT.format(failure_text=failure_text)
    return await make_request(query_url, query_text, interaction_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
