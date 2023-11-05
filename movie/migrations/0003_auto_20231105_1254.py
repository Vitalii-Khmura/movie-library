# Generated by Django 4.2.4 on 2023-11-05 10:54
from django.core.management import call_command
from django.db import migrations


def func(apps, schema_editor):
    call_command('loaddata', 'fixture_data.json')

def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0002_actor_avatar_alter_movie_poster"),
    ]

    operations = [
        migrations.RunPython(func, reverse_func)
    ]