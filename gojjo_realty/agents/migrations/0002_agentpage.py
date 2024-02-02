# Generated by Django 4.2.9 on 2024-02-02 01:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AgentPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                ("title", models.CharField(blank=True, max_length=255, verbose_name="Title")),
                ("slug", models.SlugField(blank=True, max_length=255, verbose_name="Slug")),
                ("content", ckeditor.fields.RichTextField(blank=True, verbose_name="Content")),
                ("is_published", models.BooleanField(default=True, verbose_name="Publish")),
            ],
            options={
                "verbose_name": "agent page",
                "verbose_name_plural": "agent pages",
                "ordering": ["title"],
            },
        ),
    ]