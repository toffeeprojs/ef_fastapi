from fastapi import FastAPI

from handlers import router as handlers
from depends import depends_lifespan


app = FastAPI(lifespan=depends_lifespan)
app.include_router(handlers)
