# Generated by Django 3.1.3 on 2020-11-13 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0006_facedetection_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facedetection',
            name='author',
        ),
    ]
