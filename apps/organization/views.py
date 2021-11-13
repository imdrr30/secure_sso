from apps.common.views.viewsets import BaseModelViewSet
from .models import Organization
from apps.common.views.permissions import UserTypeAccess
from apps.administration.actions import ORGANIZATION_EXTRA_SERIALIZER_FIELDS

# Create your views here.


class OrganizationViewSet(BaseModelViewSet):

    model_data = Organization
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = Organization
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
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
                "queryset": model.objects.all(),
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
                "queryset": model.objects.filter(id=self.request.user.organization.id),
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
