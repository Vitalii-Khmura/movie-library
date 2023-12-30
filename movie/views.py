from django.contrib.auth import views, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from movie.form import (
    MovieSearchForm,
    LoginForm,
    RegistrationsForm,
    ReviewForm
)
from movie.models import Movie, Actor, Genre, User


class GetData:
    @staticmethod
    def get_actors():
        return Actor.objects.all()

    @staticmethod
    def get_genres():
        return Genre.objects.all()


class MovieListView(LoginRequiredMixin, GetData, generic.ListView):
    model = Movie
    queryset = Movie.objects.all()
    ordering = ["title"]
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["get_genres"] = self.get_genres()
        context["get_actors"] = self.get_actors()
        context["film_title"] = title
        context["search_form"] = MovieSearchForm(initial={"title": title})

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        genres = self.request.GET.get("genres")
        if title:
            return self.queryset.filter(title__icontains=title)
        if genres:
            return self.queryset.filter(genres__name=genres)
        return self.queryset


class MovieDetailView(generic.DetailView):
    model = Movie


class UserLoginView(views.LoginView):
    form_class = LoginForm


def user_logout_view(request):
    logout(request)
    return redirect("/accounts/login/")


class RegistrationView(generic.CreateView):
    model = User
    template_name = "registration/sign_up.html"
    form_class = RegistrationsForm
    success_url = reverse_lazy("login")


class AddReview(generic.View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if request.user.is_authenticated:
            if form.is_valid():
                form.save(commit=False)
                form.movie = movie
                form.user = request.user
                form.save()
            return redirect(movie.get_absolute_url())
        return reverse_lazy("login")
