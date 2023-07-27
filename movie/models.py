from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

from movie_library import settings


class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=100, default="")
    description = models.TextField()
    poster = models.ImageField(upload_to="movies")
    year = models.PositiveSmallIntegerField("Release date")
    country = models.CharField(max_length=64)
    genres = models.ManyToManyField(Genre, related_name="genre")
    actors = models.ManyToManyField(Actor, related_name="film_actors")
    directors = models.ManyToManyField(Actor, related_name="film_directors")
    fess_in_world = models.PositiveSmallIntegerField(
        default=0,
        help_text="enter the dollar amount"
    )
    budget = models.PositiveSmallIntegerField(
        default=0,
        help_text="enter the dollar amount"
    )
    world_premiere = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.title}"


class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField(max_length=4000)

    def __str__(self):
        return f"{self.user} - {self.movie}"

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
