from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Profiles.models import Profile


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
