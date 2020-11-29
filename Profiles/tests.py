from django.test import TestCase

from Profiles.forms import CustomRegisterForm


class TestForms(TestCase):

    def test_custom_register_form_with_correct_value_should_be_valid(self):
        data = {'username': 'ivan', 'email': 'ivan@abv,bg', 'password1': '159753qwe', 'password2': '159753qwe'}
        form = CustomRegisterForm(data)
        self.assertTrue(form.is_valid())

    def test_custom_register_form_with_invalid_pass_should_not_return(self):
        data = {'username': 'ivan', 'email': 'ivan@abv,bg', 'password1': '159753qwe', 'password2': '159753qwe'}
        form = CustomRegisterForm(data)
        self.assertFalse(form.is_valid())

    def test_custom_register_form_with_similar_username_and_pass_should_not_return(self):
        data = {'username': 'ivan', 'email': 'ivan@abv,bg', 'password1': 'ivan', 'password2': 'ivan'}
        form = CustomRegisterForm(data)
        self.assertFalse(form.is_valid())

