# Generated by Django 3.1.7 on 2021-02-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0003_auto_20210219_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseId',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
