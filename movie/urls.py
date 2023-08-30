from django.contrib import admin
from django.urls import path, include
from movie import views

urlpatterns = [
    path("", views.MovieListView.as_view(), name="index"),
    path(
        "movie_detail/<int:pk>/",
        views.MovieDetailView.as_view(),
        name="movie-detail"
    ),
]

app_name = "movie"
