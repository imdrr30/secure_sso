from rest_framework.serializers import ModelSerializer
from .models import CardOrganizationAssociation
from apps.organization.serializers import OrganizationSerializer


class AssociationSerializer(ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = CardOrganizationAssociation
        fields = '__all__'
        depth = 1
