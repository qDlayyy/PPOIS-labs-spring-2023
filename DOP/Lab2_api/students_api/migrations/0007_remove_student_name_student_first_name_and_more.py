# Generated by Django 4.2 on 2023-04-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_api', '0006_remove_student_first_name_remove_student_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
