# Generated by Django 3.1.3 on 2020-11-19 09:30

import Models.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0017_auto_20201119_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetection',
            name='picture',
            field=models.ImageField(upload_to='submitted_pictures', validators=[Models.validators.validate_pic_type, Models.validators.validate_size]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='jupyter_file',
            field=models.FileField(upload_to='notebooks', validators=[Models.validators.validate_size, Models.validators.validate_notebook_type]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='pickled_file',
            field=models.FileField(upload_to='binary_objects', validators=[Models.validators.validate_size, Models.validators.validate_ai_file_type]),
        ),
    ]
