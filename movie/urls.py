
from django.contrib import admin
from django.urls import path, include
from movie import views
urlpatterns = [
    path("", views.MovieListView.as_view(), name="index"),
]

app_name = "movie"
