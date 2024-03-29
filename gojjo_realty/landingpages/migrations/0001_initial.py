# Generated by Django 4.2.9 on 2024-02-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LandingPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                ("content", models.TextField(verbose_name="Content")),
            ],
            options={
                "verbose_name": "Landing Page",
                "verbose_name_plural": "Landing Pages",
            },
        ),
    ]
