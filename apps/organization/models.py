from django.db import models
from apps.common.models import BaseIdentityModel
from apps.configurations.database import *

# Create your models here.


class Organization(BaseIdentityModel):

    organization_code = models.CharField(**COMMON_NULLABLE_FIELD_CONFIG)
    parent_organization = models.ForeignKey(
        to="organization.Organization",
        on_delete=models.DO_NOTHING,
        **COMMON_NULLABLE_FIELD_CONFIG
    )
