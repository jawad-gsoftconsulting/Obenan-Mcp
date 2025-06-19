# src/hello_mcp/server_http.py
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello_world", stateless_http=True, json_response=True)

@mcp.tool(name="hello_world", description="Returns greeting")
def hello_world() -> str:
    return "Hello World Tool is called"

app = FastAPI()
app.add_api_route("/sse", mcp.sse_app(), methods=["GET"])
