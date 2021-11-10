from django.db import models
from apps.common.models import BaseIdentityModel
from apps.configurations.database import *

# Create your models here.


class Organization(BaseIdentityModel):

    organization_code = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, **COMMON_NULLABLE_FIELD_CONFIG)
    parent_organization = models.ForeignKey(
        to="organization.Organization",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG
    )
