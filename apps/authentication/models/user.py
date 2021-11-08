from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from apps.common.models import BaseModel
from apps.configurations.database import *
from phonenumber_field.modelfields import PhoneNumberField


class User(BaseModel, AbstractBaseUser):
    # config fields
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    # auth related | note: username and email are the same
    username = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, unique=True)
    email = models.EmailField(unique=True)

    password = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH, **COMMON_NULLABLE_FIELD_CONFIG
    )

    is_staff = models.BooleanField(default=False)

    phone_number = PhoneNumberField(**COMMON_NULLABLE_FIELD_CONFIG)

    user_type = models.ForeignKey(
        to="adminstration.UserType",
        related_name="created_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG
    )
    date_joined = models.DateTimeField(default=timezone.now)
