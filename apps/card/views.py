from rest_framework.viewsets import ModelViewSet
from .models import CardType, Card
from .serializers import CardSerializer, CardTypeSerializer
from apps.common.views.permissions import UserTypeAccess
# Create your views here.


class CardViewSet(ModelViewSet):

    serializer_class = CardSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY", "ADMIN_GATWAY","SUPERADMIN_ORG", "ADMIN_ORG")
    permission_classes = (UserTypeAccess,)
    queryset = Card.objects.all()


class CardTypeViewSet(ModelViewSet):

    serializer_class = CardTypeSerializer
    USER_ACCESS_CODES = ("SUPERADMIN_GATWAY", "ADMIN_GATWAY",)
    permission_classes = (UserTypeAccess,)
    queryset = CardType.objects.all()