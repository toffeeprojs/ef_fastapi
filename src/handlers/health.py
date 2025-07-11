from fastapi import APIRouter

route = APIRouter(
    prefix="/health"
)


@route.get("/")
async def health_check():
    return "Ok"
