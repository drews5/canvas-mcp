from canvas_mcp.server import create_server, register_all_tools
import uvicorn

# 1. Setup the Server
mcp = create_server()
register_all_tools(mcp)

# 2. THE FIX: Access the raw web app directly
# This bypasses the strict validation logic of the CLI
try:
    # Try to get the hidden app (newer versions of fastmcp)
    app = mcp._sse_app
except AttributeError:
    # Fallback if the internal name is different
    app = mcp

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
