from rest_framework.serializers import ModelSerializer
from .models import CardOrganizationAssociation
from apps.card.models import Card
from apps.organization.serializers import OrganizationSerializer


class AssociationSerializer(ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = CardOrganizationAssociation
        fields = '__all__'


class CardSerializer(ModelSerializer):
    associations = AssociationSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
