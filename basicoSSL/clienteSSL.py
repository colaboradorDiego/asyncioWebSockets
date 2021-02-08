# WSS requiere TLS self-signed certificate

import asyncio
import websockets

import pathlib
import ssl


numeros=['1', '2', '3', '4', '5', '6', '7', '8']

#ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)


async def cliente():
    uri = "wss://localhost:8765"
    #async with websockets.connect(uri, ssl=ssl_context) as websocket:
    async with websockets.connect(uri, ssl=True) as websocket:
        
        for numero in numeros:
            try:
                await websocket.send("Contando: " + numero)

            except ConnectionResetError as connReset:
                print('El server reseteo la conn')
                print('fin del cliente')

            except websockets.exceptions.ConnectionClosedError as connClose:
                print('El server esta cerrado')
                print('fin del cliente')
                
            respuesta = await websocket.recv()
            print(respuesta)

asyncio.get_event_loop().run_until_complete(cliente())
