from django.contrib.auth import get_user_model
from django.test import TestCase

from movie.models import Genre, Movie, Actor, Reviews

MOVIE = {
    "title": "Avatar",
    "tagline": "Enter the world of Avatar.",
    "description": "A paraplegic Marine dispatched to the moon Pandora on a unique "
                   "mission becomes torn between following his orders and protecting"
                   " the world he feels is his home.",
    "year": 2009,
    "country": "USA",
    "fess_in_world": 2923706026,
    "budget": 237000000,
    "poster": "poster/Avatar_Qtaynzv.jpg",
}


class TestModel(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TeSt",
            password="Test123word",
        )
        self.movie = Movie.objects.create(**MOVIE)
        self.genre = Genre.objects.create(
            name="Action",
            description="It is test",
        )
        self.actors = Actor.objects.create(
            avatar="actors/brad_pitt.png",
            first_name="John",
            last_name="Smith",
            age=52
        )
        self.reviews = Reviews.objects.create(
            user=self.user,
            movie=self.movie,
            text="The best film",
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), self.movie.title)

    def test_genre_str(self):
        self.assertEqual(str(self.genre), self.genre.name)

    def test_actors_str(self):
        self.assertEqual(str(self.actors), f"{self.actors.first_name} - {self.actors.last_name}")

    def test_reviews_str(self):
        self.assertEqual(str(self.reviews), f"{self.user} - {self.movie}")
