from .views import *
from django.urls import path

urlpatterns = [
    path("ping/", PingView.as_view()),
    path("auth/login/", LoginView.as_view()),
    path("auth/logout/", LoginView.as_view()),
]
