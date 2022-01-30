import typing

import strawberry
from strawberry.django import auth

from .types import User
from .types import UserSignupInput
from .types import UserLoginInput


@strawberry.type
class Query:
    users: typing.List[User] = strawberry.django.field()


@strawberry.type
class Mutation:
    login: User = auth
