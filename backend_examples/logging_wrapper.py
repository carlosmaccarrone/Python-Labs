from fastapi import Request
import logging

class LoggerWrapper:
    def __init__(self, name=__name__, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def log_request(self, request: Request):
        self.info(f"Request: method={request.method} url={request.url} headers={dict(request.headers)}")

    def log_response(self, status_code: int, content: str):
        self.info(f"Response: status_code={status_code} content={content}")


## LOGGING TEST
################
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
logger = LoggerWrapper("myapi")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.log_request(request)
    response = await call_next(request)
    body = [section async for section in response.body_iterator]
    logger.log_response(response.status_code, body)
    # Para que la respuesta funcione después de consumir body_iterator
    response.body_iterator = AsyncIteratorWrapper(body)
    return response

@app.get("/")
async def root():
    logger.info("Handling root endpoint")
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app)

