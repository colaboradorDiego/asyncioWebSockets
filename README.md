# websockets (Built on top of asyncio)
	https://pypi.org/project/websockets/
	https://websockets.readthedocs.io/en/stable/index.html
	Importante 1:
	- Are there onopen, onmessage, onerror, and onclose callbacks?
	--- No, there aren’t.
	--- Websockets provides high-level, coroutine-based APIs.
	--- If you prefer callback-based APIs, you should use another library.
	
	Importante 2:
	- Can I use websockets synchronously, without async/await?
	--- Yes, convert asynchronous to synchronous call by wrapping it in asyncio.get_event_loop().run_until_complete(...)
	--- If this turns out to be impractical, you should use another library.

# Codeando 
	Seguimos esta guia --> https://websockets.readthedocs.io/en/stable/intro.html
	
# Basico
	Arrancamos con una cliente/server super basico por http equivalente a ws
	
# BasicoSSL
	cliente/server que utilizan SSL (certificados TLS) esto es https equivalente a wss
	
	Como estamos en un localhost el certificado hay que generarlo.
	leer pem certificate --> https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate

# WebServer
	tenemos un server que puede ser browseable por cualquier navegador
	es sumamente interesante abrir dos navegadores para ver como la concurrencia funciona a la perfeccion, el server
	va atendiendo a los clientes de manera concurrente.
	
# Sincro
	Al webserver anterior le agregamos msg de sincro con todos los clientes
	
# commonPaterns


# From GitHub
search: https://github.com/search?l=Python&p=3&q=websockets+asyncio&type=Repositories

Simples
*******
liuhuihuii/python_asyncio_websockets
requriment python > 3.5,asyncio and websockets to get parallem io read from Binance and okex 
	https://github.com/liuhuihuii/python_asyncio_websockets
	


Muy dificil
***********
leonh/redis-streams-fastapi-chat
A simple Redis Streams backed Chat app using Websockets, Asyncio and FastAPI/Starlette. 
	https://github.com/leonh/redis-streams-fastapi-chat
	

closeio/socketshark
A WebSocket message router based on Python/Redis/asyncio 	
	https://github.com/closeio/socketshark
	
	

	
	

	