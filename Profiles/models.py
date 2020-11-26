from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='profile_pictures/default.jpeg', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username}'

