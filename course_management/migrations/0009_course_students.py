# Generated by Django 3.1.7 on 2021-02-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
        ('course_management', '0008_evaluationcomponent_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='user_management.User'),
        ),
    ]