from .models import Card
from apps.association.models import CardOrganizationAssociation
from ..authentication.models import User


def create_card_from_organization(cls, validated_data):

    organization = cls.request.user.organization

    if organization is not None:
        validated_data["provided_organization"] = organization

    user_id_for_organization = validated_data.pop("user_id_for_organization", None)
    customer_data = validated_data.pop("customer_data", None)

    card = Card(**validated_data)
    users = User.objects.get(phone_number=validated_data["phone_number"])
    if len(users) > 0:
        card.card_owned_by = users[0]
    card.save()

    card_association_data = {
        "card": card,
        "organization": organization,
        "user_id_for_organization": user_id_for_organization,
        "customer_data": customer_data,
        "is_association_accepted_by_user": True,
        "is_association_accepted_by_organization": True,
    }

    card_association = CardOrganizationAssociation(**card_association_data)
    card_association.save()

    return card


CARD_ACTIONS = {"create": classmethod(create_card_from_organization)}
