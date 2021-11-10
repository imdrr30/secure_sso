from django.db import models
from apps.common.models import BaseModel

# Create your models here.
from apps.configurations.database import *


class CardOrganizationAssociation(BaseModel):

    card = models.ForeignKey(
        to="card.Card", related_name="access_card", on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        to="organization.Organization",
        related_name="associated_organization",
        on_delete=models.DO_NOTHING,
    )
    user_id_for_organization = models.TextField(**COMMON_NULLABLE_FIELD_CONFIG)
