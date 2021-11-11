from rest_framework.viewsets import ModelViewSet
from .models import UserType
from .serializers import UserTypeSerializer, User, UserSerializer
from apps.common.views.permissions import UserTypeAccess
# Create your views here.


class UserTypeViewSet(ModelViewSet):

    serializer_class = UserTypeSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY",)
    permission_classes = (UserTypeAccess,)
    queryset = UserType.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY", "ADMIN_GATWAY", "SUPERADMIN_ORG", "ADMIN_ORG", "END_USER", "EMP_ORG")
    permission_classes = (UserTypeAccess,)
    queryset = User.objects.all()
