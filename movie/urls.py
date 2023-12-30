from django.urls import path

from movie import views

urlpatterns = [
    path("", views.MovieListView.as_view(), name="index"),
    path(
        "movie_detail/<int:pk>/",
        views.MovieDetailView.as_view(),
        name="movie-detail"
    ),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add-review"),
]

app_name = "movie"
