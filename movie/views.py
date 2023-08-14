from django.views import View, generic

from movie.form import MovieSearchForm
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

        title = self.request.GET.get("title", "")

        context["get_genres"] = self.get_genres()
        context["film_title"] = title
        context["search_form"] = MovieSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        genres = self.request.GET.get("genres")
        if title:
            return self.queryset.filter(title__icontains=title)
        if genres:
            return self.queryset.filter(genres__name=genres)
        return self.queryset
