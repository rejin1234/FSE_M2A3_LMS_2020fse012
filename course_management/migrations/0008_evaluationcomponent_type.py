# Generated by Django 3.1.7 on 2021-02-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0007_evaluationcomponent'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluationcomponent',
            name='type',
            field=models.CharField(default='QUIZ', max_length=20),
        ),
    ]