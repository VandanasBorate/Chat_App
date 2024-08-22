
import asyncio
import websockets  # type: ignore

# Set to store all connected clients
clients = set()

async def handle_client(websocket, path):
    # Register the client
    clients.add(websocket)
    print(f"New client connected: {websocket.remote_address}. Total clients: {len(clients)}")

    try:
        async for message in websocket:
            # Broadcast the incoming message to all connected clients except the sender
            if clients:  # Ensure there are connected clients
                await asyncio.wait([
                    asyncio.create_task(client.send(message)) 
                    for client in clients if client != websocket
                ])
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Unregister the client on disconnection
        clients.remove(websocket)
        print(f"Client {websocket.remote_address} removed. Total connected clients: {len(clients)}")

async def main():
    # Start the WebSocket server
    print("Starting WebSocket server on ws://localhost:8765...")
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket server is running.")
        await asyncio.Future()  # Run forever

# Run the server
asyncio.run(main())
