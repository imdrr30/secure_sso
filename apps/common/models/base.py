import uuid
from django.db import models
from apps.configurations.database import *
import json


def load_initial_data(model):

    model_name = model.__name__.lower()
    json_data = json.load(open(f"apps/initial_data/{model_name}.json", "r"))
    model.objects.all().delete()
    is_user = model_name == "user"

    for data in json_data:
        obj = model(**data)
        if is_user:
            if "is_superuser" in data.keys() and data["is_superuser"]:
                print("Creating Superuser.")
                model.objects.create_superuser(**data)
                print("Superuser created.")
            else:
                password = data.pop("password")
                obj.set_password(password)
                obj.save()
        else:
            obj.save()


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
