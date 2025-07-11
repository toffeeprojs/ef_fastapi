from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from decimal import Decimal

route = APIRouter(
    prefix="/users"
)


class UserExchangePath(BaseModel):
    user_id: int

    currency_give: Annotated[
        str,
        Field(
            min_length=3,
            max_length=5,
            pattern=r"^[A-Z0-9]{3,5}$",
            validation_alias="give"
        )
    ]
    currency_get: Annotated[
        str,
        Field(
            min_length=3,
            max_length=5,
            pattern=r"^[A-Z0-9]{3,5}$",
            validation_alias="get"
        )
    ]

class UserExchangeModel(BaseModel):
    rate: Annotated[
        Decimal,
        Field(
            max_digits=15,
            decimal_places=6
        )
    ]

    comment: Annotated[
        str,
        Field(
            max_length=512
        )
    ] | None


@route.get("/{user_id}/exchange/{give}-{get}", response_model=Optional[UserExchangeModel])
async def user_exchange(path: UserExchangePath = Depends()) -> Optional[UserExchangeModel]:
    raise HTTPException(status_code=404)


__all__ = [
    "route"
]
