from django.contrib.auth.models import User
from django.db import models
from Models.validators import validate_pic_type, validate_size, validate_notebook_type, validate_ai_file_type


class FaceDetection(models.Model):
    picture = models.ImageField(upload_to='submitted_pictures',
                                validators=[validate_pic_type, validate_size])
    strength = models.FloatField()


class FaceProtection(models.Model):
    picture = models.ImageField(upload_to='submitted_pictures', validators=[validate_pic_type, validate_size])
    strength = models.FloatField()


class SpamFilter(models.Model):
    text = models.TextField()


class MovieReviewer(models.Model):
    text = models.TextField()


class UserModel(models.Model):
    jupyter_file = models.FileField(upload_to='notebooks', validators=[validate_size, validate_notebook_type])
    pickled_file = models.FileField(upload_to='binary_objects', validators=[validate_size, validate_ai_file_type])
    description = models.TextField(max_length=5000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
