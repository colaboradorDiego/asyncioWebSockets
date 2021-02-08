import asyncio
import websockets

numeros=['1', '2', '3', '4', '5', '6', '7', '8']

async def webServer(websocket, path, contador=0):

    for numero in numeros:
        await websocket.send('Contado: ' + numero)
        await asyncio.sleep(1)

start_server = websockets.serve(webServer, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
