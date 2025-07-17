from fastapi import APIRouter

from .exchanges import router as exchange
from .users import router as user
from .health import router as health


router = APIRouter()

for r in [
    exchange,
    user,
    health
]:
    router.include_router(r)


__all__ = [
    "router"
]
