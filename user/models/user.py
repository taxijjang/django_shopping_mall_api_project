from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from core.models import TimestampBaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password):
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class User(TimestampBaseModel, AbstractBaseUser):
    last_login = None
    username = models.CharField(max_length=20, null=True, blank=True, help_text='유저 이름')
    email = models.EmailField(unique=True, help_text='유저 이메일')
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    def has_perm(self, perm=None, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label=None):
        return self.is_admin
