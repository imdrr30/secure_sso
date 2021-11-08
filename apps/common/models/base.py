import uuid
from django.db import models
from apps.configurations.database import *


class BaseModel(models.Model):
    """
    Contains the last modified and the created fields, basically
    the base model for the entire app.
    """

    # unique id field
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    # time tracking
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # by whom
    created_by = models.ForeignKey(
        to="authentication.User",
        related_name="created_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG,
    )

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        abstract = True


class BaseIdentityModel(BaseModel):
    """
    The model class that includes identity. Identity is basically a `name`.
    This is applicable for anything like City etc.
    """

    class Meta(BaseModel.Meta):
        abstract = True

    identity = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH, verbose_name="Name/Title"
    )

    description = models.TextField(**COMMON_BLANK_AND_NULLABLE_FIELD_CONFIG)

    def __str__(self):
        return self.identity
