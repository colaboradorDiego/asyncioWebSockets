# WS server example that synchronizes state across clients

import asyncio
import json
import websockets

#dictionaty
STATE = {"value": 0}

#crea un conjunto vacio
#en este caso va a contener elementos del tipo websocket
USERS = set()


#serializa el dictionary state y le agrega un header.
def state_event():
    return json.dumps({"type": "state", **STATE})


#serializa info relativa a la cantidad del conjunto USERS
def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


#envia un msg serializado a cada websocket del conjunto USERS
async def notify_state():
    # asyncio.wait doesn't accept an empty list
    if USERS:
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


#envia un msg serializado a cada websocket del conjunto USERS
async def notify_users():
    # asyncio.wait doesn't accept an empty list
    if USERS:
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


#agrega un cliente al conjunto y notifica al resto
async def register(websocket):
    USERS.add(websocket)
    await notify_users()


#quite un cliente del conjunto y notifica al resto
async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


# register(websocket) sends user_event() to websocket
async def counter(websocket, path):
    await register(websocket)
    
    try:
        await websocket.send(state_event())
        async for message in websocket:

            #recibe msg serializado
            data = json.loads(message)
            
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
                
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
                
            else:
                print("unsupported event:", data)
                
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
