from rest_framework.serializers import ModelSerializer
from .models import CardOrganizationAssociation
from apps.organization.serializers import OrganizationSerializer


class AssociationSerializer(ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = CardOrganizationAssociation
        fields = (
            "id",
            "organization",
            "created",
            "modified",
            "is_active",
            "is_deleted",
            "user_id_for_organization",
            "is_association_accepted_by_user",
            "is_association_accepted_by_organization",
        )
        depth = 1
