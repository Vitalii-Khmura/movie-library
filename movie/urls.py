from django.urls import path

from movie import views

urlpatterns = [
    path("", views.MovieListView.as_view(), name="index"),
    path(
        "movie_detail/<int:pk>/",
        views.MovieDetailView.as_view(),
        name="movie-detail"
    ),
    path(
        "movie_detail/<int:pk>/update/",
        views.MovieUpdateView.as_view(),
        name="update-movie"
    ),
    path(
        "movie_detail/<int:pk>/delete/",
        views.MovieDeleteView.as_view(),
        name="delete-movie"
    ),
    path("create/", views.MovieCreateView.as_view(), name="create-movie"),

    path("review/<int:pk>/", views.AddReview.as_view(), name="add-review"),
]

app_name = "movie"
