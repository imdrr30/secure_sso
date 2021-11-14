from apps.common.models import BaseModel
from django.db import models
from apps.configurations.database import COMMON_NULLABLE_FIELD_CONFIG


class Tracker(BaseModel):

    card = models.ForeignKey(
        to="card.Card", on_delete=models.DO_NOTHING, **COMMON_NULLABLE_FIELD_CONFIG
    )
    organization = models.ForeignKey(
        to="organization.Organization",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG
    )
    association = models.ForeignKey(
        to="association.CardOrganizationAssociation",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG
    )
    action_type = models.CharField(max_length=512)
    action_by = models.ForeignKey(to="authentication.User", on_delete=models.DO_NOTHING)
