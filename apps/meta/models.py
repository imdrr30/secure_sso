from django.db import models
from apps.common.models import BaseIdentityModel

# Create your models here.


class Country(BaseIdentityModel):
    json_file_name = "countries"
