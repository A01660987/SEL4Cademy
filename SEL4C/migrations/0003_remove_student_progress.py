# Generated by Django 4.1.7 on 2023-10-12 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SEL4C', '0002_student_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='progress',
        ),
    ]
