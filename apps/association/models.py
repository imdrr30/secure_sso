from django.db import models
from apps.common.models import BaseModel
from apps.helpers.random import get_pair_code

# Create your models here.
from apps.configurations.database import *


class CardOrganizationAssociation(BaseModel):
    class Meta(BaseModel.Meta):
        unique_together = (
            "card",
            "organization",
        )

    card = models.ForeignKey(
        to="card.Card", related_name="access_card", on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        to="organization.Organization",
        related_name="associated_organization",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG
    )

    user_id_for_organization = models.TextField(**COMMON_NULLABLE_FIELD_CONFIG)

    customer_data = models.JSONField(**COMMON_NULLABLE_FIELD_CONFIG)

    is_association_accepted_by_user = models.BooleanField(default=False)
    is_association_accepted_by_organization = models.BooleanField(default=False)


class PairCode(BaseModel):

    card = models.ForeignKey(to="card.Card", on_delete=models.CASCADE)
    code = models.CharField(max_length=8, default=get_pair_code, unique=True)
    is_used_or_revoked = models.BooleanField(default=False)
