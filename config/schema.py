import strawberry
from strawberry.tools import merge_types
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

from user.schema import Query as UserQuery
from user.schema import Mutation as UserMutation
from products.types import ProductQuery


ComboQuery = merge_types(
    "ComboQuery",
    (
        UserQuery,
        ProductQuery,
    )
)

schema = strawberry.Schema(
    query=ComboQuery,
    mutation=UserMutation,
    extensions=[
        JSONWebTokenMiddleware,
    ]
)
