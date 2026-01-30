from canvas_mcp.server import create_server, register_all_tools

# 1. Create the server
mcp = create_server()

# 2. Load the tools
register_all_tools(mcp)

# Now 'mcp' sits here globally, ready for Render to grab it.
