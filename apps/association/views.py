from apps.common.views.viewsets import BaseModelViewSet
from .models import CardOrganizationAssociation
from apps.common.views.permissions import UserTypeAccess

# Create your views here.


class CardOrganizationAssociationViewSet(BaseModelViewSet):

    model_data = CardOrganizationAssociation
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model_queryset = CardOrganizationAssociation.objects.all()
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
                "queryset": model_queryset.filter(
                    organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                    "extra_kwargs": {
                        "is_association_accepted_by_user": {
                            "is_read_only": True,
                        }
                    },
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
                "queryset": model_queryset.filter(
                    organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                    "extra_kwargs": {
                        "is_association_accepted_by_user": {
                            "is_read_only": True,
                        }
                    },
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
                "queryset": model_queryset.filter(
                    organization=self.request.user.organization
                ),
                "common_meta": {
                    "fields": "__all__",
                    "extra_kwargs": {
                        "is_association_accepted_by_user": {
                            "is_read_only": True,
                        }
                    },
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
                "queryset": model_queryset.filter(
                    card__card_owned_by=self.request.user
                ),
                "common_meta": {
                    "exclude": ("customer_data",),
                    "read_only_fields": (
                        "card",
                        "organization",
                        "user_id_for_organization",
                        "is_association_accepted_by_organization",
                    ),
                },
                "operations": {
                    "list": True,
                    "delete": True,
                    "update": True,
                    "detail": True,
                },
            },
        }
