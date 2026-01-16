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
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"Serwer czatu WebSocket startuje na porcie {port}")

    async def main():
        async with websockets.serve(handler, "0.0.0.0", port):
            await asyncio.Future()  # run forever

    asyncio.run(main())
