from apps.configurations.defaults import DEFAULT_PASSWORD
from apps.authentication.models import User
from apps.administration.models import UserType
from rest_framework import serializers


def create_super_user_for_organization(cls, validated_data):

    email = validated_data.pop("superadmin_email")
    password = validated_data.pop("superadmin_password", None)

    organization = cls.Meta.model(**validated_data)
    organization.save()
    organization.superadmin_email = email

    if password is None:
        password = DEFAULT_PASSWORD

    user_data = {
        "first_name": "Super",
        "last_name": "Admin",
        "email": email,
        "username": email,
        "organization": organization,
        "user_type": UserType.objects.get(user_access_code="SUPERADMIN_ORG")
    }
    user = User(**user_data)
    user.set_password(password)
    user.save()
    return organization


ORGANIZATION_EXTRA_SERIALIZER_FIELDS = {
    "superadmin_email": serializers.CharField(max_length=512),
    "superadmin_password": serializers.CharField(max_length=512),
    "create": classmethod(create_super_user_for_organization),
}
