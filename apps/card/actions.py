def create_card_from_organization(cls, validated_data):
    if cls.view.request.user.organization is not None:
        validated_data["organization"] = cls.view.request.user.organization.id

    return super(cls).create(validated_data)


CARD_ACTIONS = {"create": create_card_from_organization}
