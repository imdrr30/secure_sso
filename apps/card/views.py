from apps.common.views.viewsets import BaseModelViewSet
from .models import CardType, Card
from django.db.models import Q
from .actions import CARD_ACTIONS
from apps.helpers.common import get_or_none

# Create your views here.


class CardViewSet(BaseModelViewSet):

    serializer_class = Card

    def get_user_access_codes(self):
        model_queryset = Card.objects.all()
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "extra_fields": CARD_ACTIONS,
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "ADMIN_GATWAY": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "extra_fields": CARD_ACTIONS,
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "SUPERADMIN_ORG": {
                "queryset": model_queryset.filter(
                    provided_organization=get_or_none(self.request.user.organization)
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "extra_fields": CARD_ACTIONS,
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "ADMIN_ORG": {
                "queryset": model_queryset.filter(
                    provided_organization=get_or_none(self.request.user.organization)
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "extra_fields": CARD_ACTIONS,
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "EMP_ORG": {
                "queryset": model_queryset.filter(
                    provided_organization=get_or_none(self.request.user.organization)
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "extra_fields": CARD_ACTIONS,
                "operations": {
                    "list": True,
                    "create": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
            "END_USER": {
                "queryset": model_queryset.filter(
                    Q(card_owned_by=self.request.user)
                    | Q(provided_email=get_or_none(self.request.user.email))
                    | Q(provided_phone_number=get_or_none(self.request.user.phone_number))
                ),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "update": True,
                    "detail": True,
                },
            },
        }


class CardTypeViewSet(BaseModelViewSet):

    model_data = CardType

    def get_user_access_codes(self):
        model_queryset = CardType.objects.all()
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model_queryset,
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
                "queryset": model_queryset,
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
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "detail": True,
                },
            },
            "ADMIN_ORG": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "detail": True,
                },
            },
            "EMP_ORG": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "detail": True,
                },
            },
            "END_USER": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "detail": True,
                },
            },
        }
