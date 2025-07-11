from fastapi import APIRouter

from .exchanges import route as exchange
from .users import route as user
from .health import route as health

route = APIRouter(prefix="/v1")


for router in [
    exchange,
    user,
    health
]:
    route.include_router(router)


__all__ = [
    "route"
]