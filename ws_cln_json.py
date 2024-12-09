import asyncio
import websockets
import json
import time
import mysql_json_grp_month
import ssl

async def send_request():
    #uri = "ws://192.168.0.38:8007"  # Replace with your WebSocket server URL
    #uri = "wss://192.168.0.22/"  # Replace with your WebSocket server URL
    uri = "wss://wsdash.work.gd."  # Replace with your WebSocket server URL
    # Create an unverified SSL context
    ssl_context = ssl._create_unverified_context()
    
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        while True:
            # Get the current timestamp
            timestamp = int(time.time())
            
            data = mysql_json_grp_month.get_mysql_data()
            # Prepare JSON data
            # data = {
            #     "message": "Hello, WebSocket server!",
            #     "timestamp": timestamp,
            #     "status": "active"
            # }
            
            # Convert Python dictionary to JSON string
            # json_data = json.dumps(data)
            
            # Send JSON data to WebSocket server
            # await websocket.send(json_data)
            await websocket.send(data)
            
            # Optionally, receive a response from the server
            response = await websocket.recv()
            print(f"Received: {response}")
            
            # Wait for 5 seconds before sending the next request
            await asyncio.sleep(5)

async def main():
    await send_request()

# Run the event loop
asyncio.run(main())
