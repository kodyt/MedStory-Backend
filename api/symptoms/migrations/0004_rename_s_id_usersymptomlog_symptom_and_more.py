# Generated by Django 5.1.1 on 2024-11-18 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0003_symptom_units_symptom_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersymptomlog',
            old_name='s_id',
            new_name='symptom',
        ),
        migrations.RenameField(
            model_name='usersymptomlog',
            old_name='user_id',
            new_name='user',
        ),
    ]