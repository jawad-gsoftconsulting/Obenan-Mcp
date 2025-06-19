import asyncio
from typing import Any

import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# 1) Instantiate your MCP server
server = Server("hello_world")

# 2) Declare the "hello_world" tool (no inputs)
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="hello_world",
            description="Returns the classic Hello, World! string",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        )
    ]

# 3) Handle calls to the tool
@server.call_tool()
async def call_tool(
    name: str,
    arguments: dict[str, Any] | None
) -> list[types.TextContent]:
    if name != "hello_world":
        raise RuntimeError(f"Unknown tool: {name}")
    # Return the exact requested message with timestamp to avoid caching
    print("Tool called - returning 'Hello World Tool is called'")
    return [types.TextContent(type="text", text="Hello World Tool is called")]

# 4) Wire up stdio transport and entrypoint
async def main() -> None:
    async with mcp.server.stdio.stdio_server() as (reader, writer):
        await server.run(
            reader,
            writer,
            InitializationOptions(
                server_name="hello_world",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
