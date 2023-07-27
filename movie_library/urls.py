from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie_library import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("movie.urls", namespace="movie"))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
