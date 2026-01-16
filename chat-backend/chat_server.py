from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
class HealthHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    server = HTTPServer(('0.0.0.0', 10000), HealthHandler)
    server.serve_forever()
import asyncio
import websockets

USERS = set()

async def notify_users(message):
    if USERS:
        await asyncio.wait([user.send(message) for user in USERS])

async def handler(websocket, path):
    USERS.add(websocket)
    try:
        async for message in websocket:
            await notify_users(message)
    finally:
        USERS.remove(websocket)

if __name__ == "__main__":
        # Start health check server in background
        threading.Thread(target=run_health_server, daemon=True).start()
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"Serwer czatu WebSocket startuje na porcie {port}")

    async def main():
        async with websockets.serve(handler, "0.0.0.0", port):
            await asyncio.Future()  # run forever

    asyncio.run(main())
