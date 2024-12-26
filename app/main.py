from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.adapter.inbound.web import api
from app.configurator import Container, settings
from prisma import Prisma

load_dotenv()


@asynccontextmanager
async def lifespan(_: FastAPI):
    container = app.container  # DI 컨테이너 참조
    prisma: Prisma = container.prisma()
    try:
        await prisma.connect()
        yield
    finally:
        await prisma.disconnect()


container = Container()
app = FastAPI(
    title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, lifespan=lifespan
)
app.container = container
app.logger = Container.LOGGER

allow_origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"version": "1.0.0"}


app.include_router(api, prefix="/api")
