from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.config.database_config import connect_db
from app.routers.auth_routes import router as auth_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
  

app = FastAPI(lifespan=lifespan)

app.add_middleware(
   CORSMiddleware,
   allow_origins= "*",
   allow_credentials=True,
   allow_headers=["*"],
   allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
)

app.include_router(auth_route, prefix="/api/auth")

@app.get('/')
async def mridul():
    return {"message": "Jai sir raam"}