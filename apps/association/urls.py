from .views import AssociationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("card-association", AssociationViewSet, "card-association")
urlpatterns = [
    path("", include(router.urls)),
    path("get-pair-code/", views.GetNewPairCodeView.as_view()),
    path("validate-pair-code/", views.ValidatePairCodeAndAssociateView.as_view()),
    path("revoke-association-user/", views.RevokeAssociationByUser.as_view()),
    path(
        "revoke-association-organization/",
        views.RevokeAssociationByOrganization.as_view(),
    ),
    path("activate-association-user/", views.ActivateAssociationByUser.as_view()),
    path(
        "activate-association-organization/",
        views.ActivateAssociationByOrganization.as_view(),
    ),
    path("secure-auth/", views.SecureVerifyView.as_view()),
]
