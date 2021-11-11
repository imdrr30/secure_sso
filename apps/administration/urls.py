from .views import UserViewSet, UserTypeViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", UserViewSet, "user")
router.register("user-type", UserTypeViewSet, "user-type")
urlpatterns = [
    path("", include(router.urls))
]
