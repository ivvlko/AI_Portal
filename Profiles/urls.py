from django.urls import path

from Profiles.views import register_view, profile_view

urlpatterns = [
        path('register/', register_view, name='register_url'),
        path('profile/', profile_view, name='profile_url'),
]