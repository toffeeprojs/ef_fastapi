from contextlib import asynccontextmanager
from fastapi import FastAPI

from common_lib.postgres import PostgresManager, PostgresSettings


postgres_manager = PostgresManager(
    PostgresSettings()
)

@asynccontextmanager
async def depends_lifespan(app: FastAPI):
    await postgres_manager.connect()
    yield
    await postgres_manager.disconnect()


async def get_postgres():
    return postgres_manager


__all__ = [
    "depends_lifespan",
    "get_postgres"
]
