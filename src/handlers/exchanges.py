from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import Annotated
from decimal import Decimal

route = APIRouter(
    prefix="/exchanges"
)


class ExchangeListSearch(BaseModel):
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

    sorting_ratio: Annotated[
        float,
        Field(
            default=0.8,
            ge=0,
            le=1,
            validation_alias="ratio"
        )
    ]

    list_page: Annotated[
        int,
        Field(
            default=0,
            ge=0,
            validation_alias="page"
        )
    ]

class ExchangeListModel(BaseModel):
    user_id: int

    rate: Annotated[
        Decimal,
        Field(
            max_digits=15,
            decimal_places=6
        )
    ]


@route.get("/", response_model=list[ExchangeListModel])
async def exchanges_list(query: ExchangeListSearch = Depends()) -> list[ExchangeListModel]:
    return []


__all__ = [
    "route"
]
