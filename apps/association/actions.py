from .models import CardOrganizationAssociation


def create_association(cls, validated_data):
    organization = cls.request.user.organization

    if organization is not None:
        validated_data["organization"] = organization

    association = CardOrganizationAssociation(**validated_data)
    association.save()
    return association
