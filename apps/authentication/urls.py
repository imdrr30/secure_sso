from . import views
from django.urls import path

urlpatterns = [
    path("ping/", views.PingView.as_view()),
    path("auth/login/", views.LoginView.as_view()),
    path("auth/logout/", views.LoginView.as_view()),
    path("auth/register/", views.RegistrationView.as_view()),
    path("auth/account/<pk>/update/", views.RegistrationView.as_view()),
]
