from django.db import models
from apps.common.models import BaseModel
from apps.configurations.database import *

# Create your models here.


class AbstractFormSubmissionInstance(BaseModel):
    class Meta(BaseModel.Meta):
        abstract = True


class AbstractFormField(BaseModel):
    class Meta(BaseModel.Meta):
        abstract = True

    field_type = models.CharField(**COMMON_NULLABLE_FIELD_CONFIG)
    is_multiple = models.BooleanField(default=False)
    maximum_data_if_multiple = models.PositiveIntegerField(default=1)
    is_required = models.BooleanField(default=False)
    file_upload_config = models.JSONField(**COMMON_NULLABLE_FIELD_CONFIG)


class AbstractFormData(BaseModel):
    class Meta(BaseModel.Meta):
        abstract = True

    data = models.TextField(**COMMON_NULLABLE_FIELD_CONFIG)
