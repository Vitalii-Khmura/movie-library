from django.test import TestCase

from movie.form import RegistrationsForm


class TestCreationForm(TestCase):
    def test_creation_user_with_first_name_last_name_email(self):
        form_data = {
            "username": "new_user",
            "first_name": "test",
            "last_name": "last_test",
            "email": "test@test.com",
            "password1": "Pass123word",
            "password2": "Pass123word"
        }

        form = RegistrationsForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
