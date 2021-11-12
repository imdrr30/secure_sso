from apps.common.views.viewsets import BaseModelViewSet
from .models import CardType, Card
from apps.common.views.permissions import UserTypeAccess
from django.db.models import Q

# Create your views here.


class CardViewSet(BaseModelViewSet):

    serializer_class = Card
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = Card
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "SUPERADMIN_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "ADMIN_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "EMP_ORG": {
                "queryset": model.objects.filter(
                    provided_organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "END_USER": {
                "queryset": model.objects.filter(
                    Q(card_owned_by=self.request.user)
                    | Q(provided_email=self.request.user.email)
                    | Q(provided_phone_number=self.request.user.phone_number)
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
        }


class CardTypeViewSet(BaseModelViewSet):

    model_data = CardType
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = CardType
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
        }
