from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    # Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # After login → CRUD application
    path("students/", include("students.urls")),

    # Opening 127.0.0.1:8000/ → Login page
    path(
        "",
        RedirectView.as_view(url="/login/", permanent=False),
    ),
]