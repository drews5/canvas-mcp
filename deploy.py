import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from mcp.server.sse import SseServerTransport
from canvas_mcp.server import create_server, register_all_tools

# 1. Initialize the Canvas Tools
mcp_wrapper = create_server()
register_all_tools(mcp_wrapper)

# 2. Extract the inner Server object
# (The official FastMCP wrapper hides the real server in ._server)
server = mcp_wrapper._server if hasattr(mcp_wrapper, "_server") else mcp_wrapper

# 3. Create the SSE Transport (The "Phone Line" to Poke)
sse = SseServerTransport("/messages")

async def handle_sse(request):
    async with sse.connect_sse(request.scope, request.receive, request._send) as streams:
        await server.run(streams[0], streams[1], sse.initialization_options)

async def handle_messages(request):
    await sse.handle_post_message(request.scope, request.receive, request._send)

# 4. Create the Web App
app = Starlette(debug=True, routes=[
    Route("/sse", endpoint=handle_sse),
    Route("/messages", endpoint=handle_messages, methods=["POST"])
])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
