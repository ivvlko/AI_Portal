# Generated by Django 3.1.3 on 2020-11-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0004_remove_facedetection_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='facedetection',
            name='strength',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]