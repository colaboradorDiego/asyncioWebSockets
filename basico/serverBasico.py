import asyncio
import websockets


"""
Aca tenemos un servidor que se pone a escuchar, en modo no bloqueante,
es decir que puede hacer otras cosas mientras no llegue ningun msg.
Cuando llega el msg, lo toma, lo imprime y lo vuelve a mandar al cliente.

probar que pasa cuando comentamos la linea:
   await websocket.send(message)

"""
async def echoServer(websocket, path, contador=0):
    async for message in websocket:
        print(message)
        contador +=1
        await websocket.send(message)

        if contador>5:
            #de esta manera forzamos que el servidor se cierre.
            print('Me canse de contar, bye bye')
            asyncio.get_event_loop().stop()

start_server = websockets.serve(echoServer, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
