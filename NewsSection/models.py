from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone


class News(models.Model):
    choices = [['Computer Vision and Images', 'Computer Vision and Images'],
               ['Natural Language Processing', 'Natural Language Processing'],
               ['Robotics', 'Robotics'],
               ['Hardware and Innovations', 'Hardware and Innovations']
               ]

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=choices)
    img_url = models.URLField()
    date_posted = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f'{self.title} by {self.author} posted on {self.date_posted}'


