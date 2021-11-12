from apps.common.views.viewsets import BaseModelViewSet
from .models import UserType
from apps.authentication.models import User
from apps.common.views.permissions import UserTypeAccess

# Create your views here.


class UserTypeViewSet(BaseModelViewSet):

    model_data = UserType
    permission_classes = (UserTypeAccess,)

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
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": User.objects.all(),
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
                "queryset": User.objects.all(),
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
                "queryset": User.objects.filter(
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
                "queryset": User.objects.filter(
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
                "queryset": User.objects.filter(
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
            "END_USER": {"queryset": User.objects.filter(id=self.request.user.id)},
        }
