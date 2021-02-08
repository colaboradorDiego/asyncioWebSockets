# WSS requiere TLS certificate

import asyncio
import websockets

import pathlib
import ssl


async def echoServer(websocket, path, contador=0):
    async for message in websocket:
        print(message)
        contador +=1
        await websocket.send(message)

        if contador>5:
            print('Me canse de contar, bye bye')
            asyncio.get_event_loop().stop()

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(echoServer, "localhost", 8765, ssl=ssl_context)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
