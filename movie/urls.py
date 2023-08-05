
from django.contrib import admin
from django.urls import path, include
from movie.views import MovieListView
urlpatterns = [
    path("", MovieListView.as_view(), name="index"),

]

app_name = "movie"
