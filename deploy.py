from canvas_mcp.server import create_server, register_all_tools

# 1. Create the server
mcp = create_server()

# 2. Register tools
register_all_tools(mcp)

# 3. THAT'S IT. Do not add mcp.run(), do not add uvicorn.
