from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI
import uvicorn
import json

class AsyncIteratorWrapper:
	"""
	link: https://www.python.org/dev/peps/pep-0492/#example-2
	"""

	def __init__(self, obj):
		self._it = iter(obj)

	def __aiter__(self):
		return self

	async def __anext__(self):
		try:
			value = next(self._it)
		except StopIteration:
			raise StopAsyncIteration
		return value

class MyMiddleware(BaseHTTPMiddleware):
	def __init__(self, app):
		super().__init__(app)

	async def set_body(self, request):
		receive_ = await request._receive()
		async def receive():
			return receive_
		request._receive = receive


	async def dispatch(self, request, call_next):
		request_body = {}
		if request.method == 'POST':
			await self.set_body(request)
			request_body = await request.json()

		print(request_body)
		response = await call_next(request)

		resp_body = [section async for section in response.body_iterator]
		setattr(response, "body_iterator", AsyncIteratorWrapper(resp_body))

		to_load = next(iter(resp_body), b'[]')
		try:
			resp_body = json.loads(to_load)
		except:
			resp_body = {"nothing":"nothing"}
		print(resp_body)
		return response


app = FastAPI()
app.add_middleware(MyMiddleware)

@app.post("/add")
def add_points(item: dict):
	return item

@app.get("/users")
def add_users():
	return {"user":"one"}

if __name__ == '__main__':
	uvicorn.run(app, port=8080)


## TEST API
############
import requests

def post_example():
    url = 'http://127.0.0.1:8080/add/'
    parametros = json.dumps({'symbol': 'MSFT', 'date': '2020-02-19'})
    respuesta = requests.post(url, data=parametros)
    print(respuesta.text)

def get_example():
    url = 'http://127.0.0.1:8080/users/'
    respuesta = requests.get(url)
    print(respuesta.text)

