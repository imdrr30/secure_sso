from apps.common.views.viewsets import BaseModelViewSet
from .models import UserType
from apps.authentication.models import User

# Create your views here.


class UserTypeViewSet(BaseModelViewSet):

    model_data = UserType

    def get_user_access_codes(self):
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": UserType.objects.all(),
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


class UserViewSet(BaseModelViewSet):
    model_data = User

    def get_user_access_codes(self):
        model_queryset = User.objects.all()
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model_queryset,
                "common_meta": {
                    "fields": "__all__",
                    "extra_kwargs": {"password": {"write_only": True}},
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
                    "extra_kwargs": {"password": {"write_only": True}},
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
                    "extra_kwargs": {"password": {"write_only": True}},
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
                    "extra_kwargs": {"password": {"write_only": True}},
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
                    "extra_kwargs": {"password": {"write_only": True}},
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
                "queryset": model_queryset.filter(id=self.request.user.id),
                "common_meta": {
                    "fields": "__all__",
                    "extra_kwargs": {"password": {"write_only": True}},
                },
                "operations": {
                    "list": True,
                    "delete": True,
                    "detail": True,
                },
            },
        }
