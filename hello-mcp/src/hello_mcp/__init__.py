import asyncio
from .server import main as _async_main

def main() -> None:
    """Console script entrypoint: run the MCP stdio server."""
    asyncio.run(_async_main())
