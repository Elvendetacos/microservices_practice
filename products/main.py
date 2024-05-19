from fastapi import FastAPI

from infraestructure.configuration.rabbit import Rabbit
from infraestructure.web.listener.rabbit_listener import start_listening
from infraestructure.web.rest.controller import routes
import uvicorn

app = FastAPI()

rabbitmq = Rabbit()


@app.on_event("startup")
async def startup_event():
    start_listening()

app.include_router(routes.controller)

if __name__ == "__main__":
    uvicorn.run(app, port=3001)
