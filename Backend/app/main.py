from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from contextlib import asynccontextmanager

from app.config.database_config import connect_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
  

app = FastAPI(lifespan=lifespan)





# app.add_middleware()

@app.get('/')
async def mridul():
    return {"message": "Jai sir raam"}