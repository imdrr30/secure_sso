from rest_framework import serializers
from .models import CardOrganizationAssociation


class CardOrganizationAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CardOrganizationAssociation
