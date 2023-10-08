# Generated by Django 4.2.6 on 2023-10-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEL4C', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='description',
        ),
        migrations.AlterField(
            model_name='discipline',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Disciplina'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Institución'),
        ),
    ]
