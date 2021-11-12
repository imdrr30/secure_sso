from apps.common.views.viewsets import BaseModelViewSet
from .models import Organization
from .serializers import OrganizationSerializer
from apps.common.views.permissions import UserTypeAccess

# Create your views here.


class OrganizationViewSet(BaseModelViewSet):

    serializer_class = OrganizationSerializer
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = Organization
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
        }
