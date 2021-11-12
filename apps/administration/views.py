from apps.common.views.viewsets import BaseModelViewSet
from .models import UserType
from .serializers import UserTypeSerializer, User, UserSerializer
from apps.common.views.permissions import UserTypeAccess

# Create your views here.


class UserTypeViewSet(BaseModelViewSet):

    serializer_class = UserTypeSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY",)
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": UserType.objects.all(),
            },
        }


class UserViewSet(BaseModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserTypeAccess,)

    def get_user_access_codes(self):
        return {
            "SUPERADMIN_GATWAY": {
                "queryset": User.objects.all(),
            },
            "ADMIN_GATWAY": {
                "queryset": User.objects.all(),
            },
            "SUPERADMIN_ORG": {
                "queryset": User.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "ADMIN_ORG": {
                "queryset": User.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "EMP_ORG": {
                "queryset": User.objects.filter(
                    organization=self.request.user.organization
                )
            },
            "END_USER": {"queryset": User.objects.filter(id=self.request.user.id)},
        }
