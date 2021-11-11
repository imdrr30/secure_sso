from rest_framework import serializers
from .models import UserType
from apps.authentication.models import User


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser")
        extra_kwargs = {"password": {"write_only": True}}
