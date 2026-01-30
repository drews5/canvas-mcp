from canvas_mcp.server import create_server, register_all_tools

# 1. Create the MCP Server Object
mcp = create_server()

# 2. Register all the tools
register_all_tools(mcp)

# 3. IMPORTANT: Expose the ASGI app for Uvicorn
# This unwraps the underlying Starlette app that Render needs
app = mcp._sse_app if hasattr(mcp, "_sse_app") else mcp
