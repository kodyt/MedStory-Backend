# Generated by Django 5.1.1 on 2024-10-01 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0004_user_rename_time_patientsymptom_onset_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsymptom',
            name='onset_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 1, 14, 6, 51, 230348)),
        ),
    ]