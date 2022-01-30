import decimal
import typing

import strawberry
from strawberry.django import auto

from .. import models


@strawberry.django.type(models.Product)
class Product:
    id: auto
    title: str
    price: decimal.Decimal
    image: str


@strawberry.type
class Query:
    products: typing.List[Product] = strawberry.django.field()
