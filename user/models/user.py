from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from core.models import TimestampBaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, name, email, password):
        user = self.model(
            name=name,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class User(TimestampBaseModel, AbstractBaseUser):
    last_login = None
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
