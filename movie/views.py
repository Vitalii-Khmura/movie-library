from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render
from django.views import View, generic

from movie.form import MovieSearchForm, GenreFilterForm
from movie.models import Movie, Actor, Genre


class GetData:

    @staticmethod
    def get_genres():
        return Genre.objects.all()


class MovieListView(GetData, generic.ListView):
    model = Movie
    queryset = Movie.objects.all()
    ordering = ["title"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_genres"] = self.get_genres()

        return context
