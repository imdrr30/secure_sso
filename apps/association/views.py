from apps.common.views.viewsets import BaseModelViewSet
from .models import CardOrganizationAssociation
from .serializers import CardOrganizationAssociationSerializer
from apps.common.views.permissions import UserTypeAccess

# Create your views here.


class CardOrganizationAssociationViewSet(BaseModelViewSet):

    serializer_class = CardOrganizationAssociationSerializer
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        model = CardOrganizationAssociation
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "ADMIN_GATWAY": {
                "queryset": model.objects.all(),
            },
            "SUPERADMIN_ORG": {
                "queryset": model.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "ADMIN_ORG": {
                "queryset": model.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "EMP_ORG": {
                "queryset": model.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "END_USER": {
                "queryset": model.objects.filter(card__card_owned_by=self.request.user)
            },
        }
