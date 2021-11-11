from rest_framework.viewsets import ModelViewSet
from .models import CardOrganizationAssociation
from .serializers import CardOrganizationAssociationSerializer
from apps.common.views.permissions import UserTypeAccess
# Create your views here.


class CardOrganizationAssociationViewSet(ModelViewSet):

    serializer_class = CardOrganizationAssociationSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY", "ADMIN_GATWAY", "SUPERADMIN_ORG", "ADMIN_ORG", "END_USER", "EMP_ORG")
    permission_classes = (UserTypeAccess,)
    queryset = CardOrganizationAssociation.objects.all()