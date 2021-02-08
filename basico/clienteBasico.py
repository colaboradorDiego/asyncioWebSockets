import asyncio
import websockets

numeros=['1', '2', '3', '4', '5', '6', '7', '8']

"""
Lo interesante de este cliente es la linea:
   respuesta = await websocket.recv()

   si no tiene respuesta del servisor el loop no sigue.
   queda esperando a q llegue un msg para poder continuar
   y esto es asi ya que el cliente no tiene otra cosa que hacer

"""
async def cliente():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

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
