from canvas_mcp.server import create_server, register_all_tools

# Just create the object. Do not run it.
mcp = create_server()
register_all_tools(mcp)
