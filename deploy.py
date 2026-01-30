import os
from canvas_mcp.server import create_server, register_all_tools

# 1. Initialize the app
mcp = create_server()
register_all_tools(mcp)

if __name__ == "__main__":
    # 2. Get the PORT from Render (default to 10000 if missing)
    port = int(os.environ.get("PORT", 10000))
    
    # 3. Force the server to run in SSE mode
    print(f"Starting SSE server on port {port}...")
    mcp.run(transport="sse", host="0.0.0.0", port=port)
