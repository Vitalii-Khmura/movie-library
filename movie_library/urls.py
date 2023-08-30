from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie import views
from movie_library import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movie.urls", namespace="movie")),

    # Accounts
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
    path("accounts/logout/", views.user_logout_view, name="logout"),
    path(
        "accounts/register/",
        views.RegistrationView.as_view(),
        name="register"
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
