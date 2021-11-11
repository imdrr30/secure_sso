from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("", include("apps.organization.urls")),
    path("", include("apps.card.urls")),
    path("", include("apps.association.urls")),
    path("", include("apps.administration.urls")),
]
