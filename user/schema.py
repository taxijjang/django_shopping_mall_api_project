import typing

from django.contrib import auth

import strawberry
from strawberry.django import auth
from strawberry.django import django_resolver
from strawberry_django_jwt import mutations as jwt_mutations

from .types import User
from .types import UserSignupInput
from .types import UserLoginInput


@strawberry.type
class Query:
    users: typing.List[User] = strawberry.django.field()
    me: User = auth.current_user()


@strawberry.type
class Mutation:
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie