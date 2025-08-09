from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import json

class MiniResponse(BaseModel):
    headers: dict = {}
    status_code: int = 0
    body: dict = {}

app = FastAPI()

class ASGIMiddleware:
    """
    TODO:
    - Handle streaming request and response bodies properly to avoid loading large payloads entirely into memory.
    - In 'send_wrapper', currently assumes the response body arrives as a single complete JSON message.
      However, in ASGI, the body may be fragmented across multiple messages, which can lead to parsing errors.
    - Implement chunked processing and buffering logic to correctly assemble and parse fragmented bodies.
    """ 
    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http": # == "http"
            return await self.app(scope, receive, send)        
        if scope["type"] != "http.request":
            if scope["method"] in ('POST', 'PUT', 'DELETE'):
                receive_ = await receive()
                async def receive_func():
                    return receive_
                receive = receive_func
            request = Request(scope, receive, send)
            ### DO SOMETHING WITH THE REQUEST
            print({ "http_request_method": request.method, "http_request_path": request.url.path, \
                "http_request_query_string": request.query_params, "http_request_remote_address": request.client.host,\
                "http_request_headers": request.headers, "http_request_body": await request.json()})

        response = MiniResponse()

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = {}
                for key,value in message["headers"]:
                    headers.setdefault(key.decode(), value.decode())
                response.headers = headers
                response.status_code = message["status"]

            if message["type"] == "http.response.body":
                response.body = json.loads(message["body"])

            return await send(message)
        await self.app(scope, receive, send_wrapper)

        if response.headers and response.status_code and response.body:
            ### DO SOMETHING WITH THE RESPONSE
            print(response.model_dump())


app.add_middleware(ASGIMiddleware)

@app.get("/test1")
async def test():
    result = {"result": "It works!!"}
    return JSONResponse(content=result)

@app.post("/test2")
async def test():
    result = {"result": "It works!!"}
    return JSONResponse(content=result)    

if __name__ == "__main__":
    uvicorn.run(app, port=8080)


### pip install pydantic pydantic_settings fastapi uvicorn

