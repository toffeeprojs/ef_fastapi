from fastapi import FastAPI

from handlers import route as handlers

app = FastAPI()

app.include_router(handlers)


@app.get("/health")
async def health_check() -> str:
    return "Ok"
