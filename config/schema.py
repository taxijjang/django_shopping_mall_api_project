import strawberry
from strawberry.tools import merge_types

from user.schema import Query as UserQuery
from products.types import ProductQuery


ComboQuery = merge_types(
    "ComboQuery",
    (
        UserQuery,
        ProductQuery,
    )
)

schema = strawberry.Schema(ComboQuery)