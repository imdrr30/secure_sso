from apps.common.responses import success_response
from apps.common.views.mixins import (
    LogoutRequired,
)
from rest_framework.authtoken.views import ObtainAuthToken
from apps.common.views import BaseAPIView
from .serializers import RegistrationSerializer
from apps.card.models import Card

# Create your views here.


class PingView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        return success_response("Pong!")


class LoginView(LogoutRequired, ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = user.create_user_token()
        return success_response(
            None, data={"token": token.key, "user_id": user.pk, "email": user.email}
        )


class RegistrationView(LogoutRequired, BaseAPIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Card.objects.filter(phone_number=user.phone_number).update(card_owned_by=user)
        token = user.create_user_token()
        return success_response(
            "Registration Completed Successfully.",
            data={"token": token.key, "user_id": user.pk, "email": user.email},
        )
