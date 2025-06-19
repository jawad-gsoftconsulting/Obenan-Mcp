# src/hello_mcp/server_http.py

from fastmcp import FastMCP

# 1) Instantiate your FastMCP server
mcp = FastMCP(name="hello_world")

# 2) Register the hello_world tool
@mcp.tool(name="hello_world", description="Returns a greeting")
def hello_world() -> str:
    return "Hello World Tool is called"

# 3) Run with SSE transport (default path: /sse, message path: /messages/)
if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=3000)
