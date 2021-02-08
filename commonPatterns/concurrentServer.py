import asyncio
import websockets


# here is consumer bussiness logic
async def consumer(message):
    print('consumer logic:', message)
    

# here is producer bussiness logic
async def producer():
    message='producer logic:'
    print(message)
    return message


async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)


async def producer_handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(message)


async def echoServer(websocket, path):
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(producer_handler(websocket, path))
    
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED
        )
    
    for task in pending:
        task.cancel()



start_server = websockets.serve(echoServer, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
