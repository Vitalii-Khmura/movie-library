from django.contrib import admin

from movie.models import Movie, Reviews, Actor, Genre

# Register your models here.
admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(Actor)
admin.site.register(Genre)
