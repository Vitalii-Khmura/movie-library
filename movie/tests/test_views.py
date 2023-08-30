from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movie.models import Movie

MOVIE_URL = reverse("movie:index")


class TestMovieListView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("test", "password123")
        self.client.force_login(self.user)

    def test_retrieve_movie(self):
        Movie.objects.create(
            title="Avatar",
            tagline="Enter the world of Avatar.",
            description="A paraplegic Marine dispatched to the moon Pandora on a unique "
            "mission becomes torn between following his orders and protecting"
            " the world he feels is his home.",
            year=2009,
            country="USA",
            fess_in_world=2923706026,
            budget=237000000,
            poster="poster/Avatar_Qtaynzv.jpg",
        )

        res = self.client.get(MOVIE_URL)
        movie = Movie.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["movie_list"]), list(movie))


class UserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("test", "password123")
        self.client.force_login(self.user)

    def test_create_user(self):
        form_data = {
            "username": "new_user",
            "first_name": "test",
            "last_name": "last_test",
            "email": "test@test.com",
            "password1": "Pass123word",
            "password2": "Pass123word",
        }

        self.client.post(reverse("register"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
