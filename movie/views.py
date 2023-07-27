from django.shortcuts import render
from django.views import View, generic

from movie.models import Movie, Actor, Genre


# Create your views here.
class MovieListView(generic.ListView):
    model = Movie

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["actors"] = Actor.objects.all()
        context["genres"] = Genre.objects.all()

        return context

