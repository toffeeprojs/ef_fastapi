from fastapi import APIRouter, Query, Path, Depends
from pydantic import BaseModel, Field
from decimal import Decimal

from common_lib.postgres import PostgresManager
from depends import get_postgres


router = APIRouter(
    prefix="/exchanges"
)


class ExchangeItem(BaseModel):
    user_id: int
    distance: float
    rate: Decimal = Field(
        max_digits=15,
        decimal_places=6
    )


@router.get("/{currency_give}-{currency_get}", response_model=list[ExchangeItem])
async def exchanges_list(
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
    sorting_ratio: float = Query(
        0.8,
        ge=0,
        le=1,
        validation_alias="ratio"
    ),
    postgres_manager: PostgresManager = Depends(get_postgres),
) -> list:
    return []


__all__ = [
    "router"
]
