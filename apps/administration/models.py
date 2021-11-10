from apps.common.models import BaseIdentityModel
from django.db import models

from apps.configurations.database import *
# Create your models here.


class UserType(BaseIdentityModel):

    user_access_level = models.PositiveIntegerField(default=1)
    user_access_code = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH, **COMMON_NULLABLE_FIELD_CONFIG)
