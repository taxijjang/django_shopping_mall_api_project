import typing

from django.contrib.auth import get_user_model

import strawberry
from strawberry.django import auth

from . import models


@strawberry.django.type(get_user_model())
class User:
    id: int
    name: str
    email: str
    password: str
    is_active: bool
    is_admin: bool
    is_superuser: bool
    is_staff: bool


@strawberry.django.input(get_user_model())
class UserSignupInput:
    name: str
    email: str
    password: str


@strawberry.django.input(get_user_model())
class UserLoginInput:
    email: str
    password: str
