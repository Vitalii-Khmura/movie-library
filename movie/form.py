from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UsernameField,
    UserCreationForm,
)
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from movie.models import Movie, Genre, User, Reviews


class MovieSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search by title..."
            }
        ),
    )


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control"
            }
        ),
    )


class RegistrationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control"
                }
            )


class  ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("movie", "user", "text", )