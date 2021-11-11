from rest_framework.viewsets import ModelViewSet
from .models import Organization
from .serializers import OrganizationSerializer
from apps.common.views.permissions import UserTypeAccess
# Create your views here.


class OrganizationViewSet(ModelViewSet):

    serializer_class = OrganizationSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY", "ADMIN_GATWAY",)
    permission_classes = (UserTypeAccess,)
    queryset = Organization.objects.all()
