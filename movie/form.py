
from django import forms
from django.forms import ModelForm, TextInput

from movie.models import Movie, Genre


class MovieSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Search by title..."
        })
    )