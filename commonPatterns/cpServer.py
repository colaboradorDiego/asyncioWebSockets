import asyncio
import websockets


"""
En este caso le metimos al servidor basico el patron Consumer/Producer
y utilizamos el mismo cliente basico
"""

# here is consumer bussiness logic
async def consumer(message):
    print('consumer logic:', message)
    

# here is producer bussiness logic
async def producer():
    message='producer logic:'
    print(message)
    return message



# Consumer: For receiving messages and passing then to a consumer coroutine
# Producer: For getting messages from a producer coroutine and sending them
async def echoServer(websocket, path):
    async for message in websocket:
        
        await consumer(message)
        message = await producer()

        await websocket.send(message)

        
start_server = websockets.serve(echoServer, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
