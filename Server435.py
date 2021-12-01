import websockets
import asyncio
print("Waiting for clients")
async def echo(websocket):
    async for message in websocket:
        print(message)
        while True:
        	await websocket.send(input("Send message"))

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
