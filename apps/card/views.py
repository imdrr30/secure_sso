from apps.common.views.viewsets import BaseModelViewSet
from .models import CardType, Card
from .serializers import CardSerializer, CardTypeSerializer
from apps.common.views.permissions import UserTypeAccess
from django.db.models import Q

# Create your views here.


class CardViewSet(BaseModelViewSet):

    serializer_class = CardSerializer
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = Card
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "SUPERADMIN_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                )
            },
            "ADMIN_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                )
            },
            "EMP_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                )
            },
            "END_USER": {
                "queryset": model.objects.filter(
                    Q(card_owned_by=self.request.user)
                    | Q(provided_email=self.request.user.email)
                    | Q(provided_phone_number=self.request.user.phone_number)
                )
            },
        }


class CardTypeViewSet(BaseModelViewSet):

    serializer_class = CardTypeSerializer
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = CardType
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
        }
