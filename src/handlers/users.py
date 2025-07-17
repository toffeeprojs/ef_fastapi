from fastapi import APIRouter, Path, HTTPException, Depends
from pydantic import BaseModel, Field
from decimal import Decimal

from common_lib.postgres import PostgresManager
from depends import get_postgres


router = APIRouter(
    prefix="/users"
)


class UserExchange(BaseModel):
    distance: float
    rate: Decimal = Field(
        max_digits=15,
        decimal_places=6
    )
    comment: str | None = Field(
        max_length=512
    )


@router.get("/{user_telegram_id}/exchange/{currency_give}-{currency_get}", response_model=UserExchange)
async def user_exchange(
    user_telegram_id: int,
    currency_give: str = Path(
        min_length=3,
        max_length=5,
        pattern=r"^[A-Z0-9]{3,5}$",
    ),
    currency_get: str = Path(
        min_length=3,
        max_length=5,
        pattern=r"^[A-Z0-9]{3,5}$",
    ),
    postgres_manager: PostgresManager = Depends(get_postgres),
) -> UserExchange:
    raise HTTPException(status_code=404)


__all__ = [
    "router"
]
