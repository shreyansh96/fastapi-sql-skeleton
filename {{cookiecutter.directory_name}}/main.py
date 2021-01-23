import uvicorn
from fastapi import FastAPI
from api.v1.api import api_router
import config
app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host=config.SERVER_IP, port=config.SERVER_PORT)


