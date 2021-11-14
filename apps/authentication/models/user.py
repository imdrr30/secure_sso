from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from apps.common.models import BaseModel
from apps.configurations.database import *
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from rest_framework.authtoken.models import Token


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    # config fields
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    # auth related | note: username and email are the same
    username = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )
    last_name = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )

    password = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH, **COMMON_NULLABLE_FIELD_CONFIG
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone_number = PhoneNumberField(**COMMON_NULLABLE_FIELD_CONFIG, unique=True)

    user_type = models.ForeignKey(
        to="administration.UserType",
        related_name="user_type",
        on_delete=models.SET_DEFAULT,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )

    organization = models.ForeignKey(
        to="organization.Organization",
        on_delete=models.CASCADE,
        **COMMON_NULLABLE_FIELD_CONFIG
    )

    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    def create_user_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token

    def revoke_user_token(self, token):
        Token.objects.filter(user=self, key=token).delete()

    def revoke_all_user_token(self):
        Token.objects.filter(user=self).delete()
