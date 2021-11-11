from .views import CardOrganizationAssociationViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("card-association", CardOrganizationAssociationViewSet, "card-association")
urlpatterns = [
    path("", include(router.urls))
]
