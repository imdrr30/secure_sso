from apps.common.views.viewsets import BaseModelViewSet
from .models import Organization
from apps.common.views.permissions import UserTypeAccess
from apps.administration.actions import ORGANIZATION_EXTRA_SERIALIZER_FIELDS

# Create your views here.


class OrganizationViewSet(BaseModelViewSet):

    model_data = Organization
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model_queryset = Organization.objects.all()
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model_queryset,
                "extra_fields": ORGANIZATION_EXTRA_SERIALIZER_FIELDS,
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
                "extra_fields": ORGANIZATION_EXTRA_SERIALIZER_FIELDS,
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
                    id=self.request.user.organization.id
                    if self.request.user.organization is not None
                    else None
                ),
                "extra_fields": ORGANIZATION_EXTRA_SERIALIZER_FIELDS,
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
