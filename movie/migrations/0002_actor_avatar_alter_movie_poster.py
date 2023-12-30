# Generated by Django 4.2.3 on 2023-08-14 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="actor",
            name="avatar",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="actors"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="movie",
            name="poster",
            field=models.ImageField(upload_to="poster"),
        ),
    ]
