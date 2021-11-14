from rest_framework.views import APIView
from apps.card.models import Card
from apps.common.responses import error_response, success_response
from .models import PairCode, CardOrganizationAssociation
from .permissions import IsOrganization, IsEndUser
from rest_framework.permissions import IsAuthenticated

from ..common.views.viewsets import BaseModelViewSet


class GetNewPairCodeView(APIView):
    permission_classes = (IsAuthenticated, IsEndUser)

    def post(self, request, *args, **kwargs):
        card_id = request.data.get("card", None)

        if card_id is None:
            return error_response("CARD_REQUIRED", "Card Required.", "400")

        card = Card.objects.get_or_none(
            id=card_id, card_owned_by=request.user, is_deleted=False, is_active=True
        )

        if card is None:
            return error_response("CARD_NOT_FOUND", "Card not found.", "404")

        PairCode.objects.filter(card_id=card_id).delete()

        paircode = PairCode(card_id=card_id)
        paircode.save()

        return success_response(
            "Pair Code Generated.",
            201,
            data={"code": paircode.code, "card": paircode.card.id},
        )


class ValidatePairCodeAndAssociateView(APIView):
    permission_classes = (IsAuthenticated, IsOrganization)

    def post(self, request, *args, **kwargs):
        pair_code = request.data.get("pair_code", None)
        user_id_for_organization = request.data.get("user_id_for_organization", None)
        customer_data = request.data.get("customer_data", None)
        organization = request.user.organization

        if None in [pair_code, user_id_for_organization]:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        paircode = PairCode.objects.get_or_none(code=pair_code)

        if paircode is None:
            return error_response(
                "INVALID_PAIR_CODE", "Pair code is invalid or expired.", 400
            )

        association_data = {
            "card": paircode.card,
            "user_id_for_organization": user_id_for_organization,
            "customer_data": customer_data,
            "organization": organization,
            "is_association_accepted_by_user": True,
            "is_association_accepted_by_organization": True,
        }

        association = CardOrganizationAssociation(**association_data)
        association.save()

        paircode.is_used_or_revoked = True
        paircode.save()

        return success_response(
            "Associated Successfully.", 201, data={"association": association.id}
        )


class RevokeAssociationByUser(APIView):
    permission_classes = (IsAuthenticated, IsEndUser)

    def post(self, request, *args, **kwargs):
        association_id = request.data.get("association", None)
        if association_id is None:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        association = CardOrganizationAssociation.objects.get_or_none(
            id=association_id, card__card_owned_by=self.request.user
        )
        if association is None:
            return error_response("INVALID_ASSOCIATION", "Invalid Association ID", 400)

        association.is_association_accepted_by_user = False
        association.save()

        return success_response("Association Revoked.", data={"association": "Revoked"})


class ActivateAssociationByUser(APIView):
    permission_classes = (IsAuthenticated, IsEndUser)

    def post(self, request, *args, **kwargs):
        association_id = request.data.get("association", None)
        if association_id is None:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        association = CardOrganizationAssociation.objects.get_or_none(
            id=association_id, card__card_owned_by=self.request.user
        )
        if association is None:
            return error_response("INVALID_ASSOCIATION", "Invalid Association ID", 400)

        association.is_association_accepted_by_user = True
        association.save()

        return success_response(
            "Association Activated.", data={"association": "Activated"}
        )


class RevokeAssociationByOrganization(APIView):
    permission_classes = (IsAuthenticated, IsOrganization)

    def post(self, request, *args, **kwargs):
        association_id = request.data.get("association", None)
        if association_id is None:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        association = CardOrganizationAssociation.objects.get_or_none(
            id=association_id, organization=self.request.user.organization
        )
        if association is None:
            return error_response("INVALID_ASSOCIATION", "Invalid Association ID", 400)

        association.is_association_accepted_by_organization = False
        association.save()

        return success_response("Association Revoked.", data={"association": "Revoked"})


class ActivateAssociationByOrganization(APIView):
    permission_classes = (IsAuthenticated, IsOrganization)

    def post(self, request, *args, **kwargs):
        association_id = request.data.get("association", None)
        if association_id is None:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        association = CardOrganizationAssociation.objects.get_or_none(
            id=association_id, organization=self.request.user.organization
        )
        if association is None:
            return error_response("INVALID_ASSOCIATION", "Invalid Association ID", 400)

        association.is_association_accepted_by_organization = True
        association.save()

        return success_response(
            "Association Activated.", data={"association": "Activated"}
        )


class AssociationViewSet(BaseModelViewSet):

    model_data = CardOrganizationAssociation

    def get_user_access_codes(self):
        model_queryset = CardOrganizationAssociation.objects.all()
        return {
            "END_USER": {
                "queryset": model_queryset.filter(card__card_owned_by=self.request.user),
                "common_meta": {
                    "fields": "__all__",
                },
                "operations": {
                    "list": True,
                    "detail": True,
                },
            },
        }


class SecureVerifyView(APIView):
    permission_classes = (IsAuthenticated, IsOrganization)

    def post(self, request, *args, **kwargs):
        card_uid = request.data.get("card_uid", None)
        if card_uid is None:
            return error_response("MISSING_FIELDS", "Missing required fields", 400)

        association = CardOrganizationAssociation.objects.get_or_none(
            card__card_uid=card_uid,
            organization=self.request.organization,
            is_deleted=False,
            is_association_accepted_by_user=True,
        )

        if association is None:
            return error_response("NO_ASSOCIATION", "No association found.", 404)

        return success_response(
            "Associated.",
            200,
            data={
                "user_id_for_organization": association.user_id_for_organization,
                "customer_data": association.customer_data,
                "is_association_accepted_by_user": association.is_association_accepted_by_user,
                "is_association_accepted_by_organization": association.is_association_accepted_by_organization,
            },
        )
