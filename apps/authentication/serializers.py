from rest_framework.serializers import ModelSerializer
from apps.authentication.models import User
from apps.administration.models import UserType


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone_number", "password")
        required = ("first_name", "last_name", "email", "phone_number", "password")

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        user.set_password(password)
        user.username = user.email
        user.user_type = UserType.objects.get(user_access_code="END_USER")
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for field, data in validated_data.items():
            setattr(instance, field, data)
        instance.set_password(password)
        instance.username = instance.email
        instance.save()
        return instance
