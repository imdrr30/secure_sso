from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import BaseModel, BaseIdentityModel

# Create your models here.
from apps.configurations.database import *


class CardType(BaseIdentityModel):
    pass


class Card(BaseModel):
    card_uid = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, unique=True)
    card_type = models.ForeignKey(to=CardType, on_delete=models.DO_NOTHING)

    provided_organization = models.ForeignKey(
        to="organization.Organization",
        related_name="provider_organization",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG,
    )
    provided_email = models.EmailField(**COMMON_NULLABLE_FIELD_CONFIG)
    provided_phone_number = PhoneNumberField(**COMMON_NULLABLE_FIELD_CONFIG)
    provided_organization_custom_data = models.JSONField(**COMMON_NULLABLE_FIELD_CONFIG)

    card_owned_by = models.ForeignKey(
        to="authentication.User",
        related_name="owned_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    )

    user_id_for_organization = models.TextField(**COMMON_NULLABLE_FIELD_CONFIG)

    customer_data = models.JSONField(**COMMON_NULLABLE_FIELD_CONFIG)
