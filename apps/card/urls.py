from .views import CardViewSet, CardTypeViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("card", CardViewSet, "card")
router.register("card-type", CardTypeViewSet, "card-type")
urlpatterns = [
    path("", include(router.urls))
]
