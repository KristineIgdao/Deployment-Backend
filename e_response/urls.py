from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    # Root health check
    path("", lambda request: JsonResponse({"status": "Backend is live!"})),

    # Admin panel
    path("admin/", admin.site.urls),

    # Djoser authentication routes
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),

    # Custom user-related routes
    path("auth/", include("accounts.urls")),     # if your custom routes are under /auth/
    path("api/", include("accounts.urls")),      # if your custom routes are under /api/
    path("accounts/", include("accounts.urls")), # needed for email verification links
]
