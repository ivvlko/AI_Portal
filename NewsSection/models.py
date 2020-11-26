from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
import django.utils.timezone
from NewsSection.validators import only_english_validator
from django.db import models
import django.utils.timezone

<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0

class News(models.Model):
    choices = [['Computer Vision and Images', 'Computer Vision and Images'],
               ['Natural Language Processing', 'Natural Language Processing'],
               ['Robotics', 'Robotics'],
<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0
               ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, validators=[only_english_validator])
    text = models.TextField(max_length=3000, validators=[only_english_validator, MinLengthValidator(100)])
<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0
               ['Hardware and Innovations', 'Hardware and Innovations']
               ]

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0
    category = models.CharField(max_length=50, choices=choices)
    img_url = models.URLField()
    date_posted = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f'{self.title} by {self.author} posted on {self.date_posted}'


<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0
class Comment(models.Model):
    name = models.CharField(max_length=50, validators=[only_english_validator])
    comment = models.TextField(max_length=500, validators=[only_english_validator])
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f'By {self.name} on {self.date_posted}'
<<<<<<< HEAD

=======
>>>>>>> 8ed763f4e7ea342aa845a41113142fd3e0c6c3a0
