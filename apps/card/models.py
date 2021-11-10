from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import BaseModel, BaseIdentityModel
from apps.forms.models import AbstractFormField, AbstractFormData

# Create your models here.
from apps.configurations.database import *


class CardType(BaseIdentityModel):
    pass


class Card(BaseModel):
    card_uid = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    card_type = models.ForeignKey(to=CardType, on_delete=models.DO_NOTHING)

    provided_organization = models.ForeignKey(
        to="organization.Organization", on_delete=models.DO_NOTHING
    )
    provided_email = models.EmailField(**COMMON_NULLABLE_FIELD_CONFIG)
    provided_phone_number = PhoneNumberField(**COMMON_NULLABLE_FIELD_CONFIG)

    card_owned_by = models.ForeignKey(
        to="authentication.User",
        related_name="owned_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    )
