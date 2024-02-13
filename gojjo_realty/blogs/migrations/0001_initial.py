# Generated by Django 4.2.9 on 2024-02-10 02:20

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogMeta",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("blog_name", models.CharField(max_length=255, verbose_name="blog name")),
                ("subtitle", models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle")),
                (
                    "header_image",
                    models.ImageField(blank=True, null=True, upload_to="blog/uploads/", verbose_name="header image"),
                ),
                ("description", models.TextField(blank=True, null=True, verbose_name="description")),
            ],
            options={
                "verbose_name": "blog meta",
                "verbose_name_plural": "blog metas",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("slug", models.SlugField(max_length=255, unique=True, verbose_name="slug")),
                ("description", models.TextField(blank=True, null=True, verbose_name="description")),
            ],
            options={
                "verbose_name": "blog category",
                "verbose_name_plural": "blog categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("subtitle", models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle")),
                ("slug", models.SlugField(max_length=255, unique=True, verbose_name="slug")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog/uploads/", verbose_name="header image"),
                ),
                ("content", tinymce.models.HTMLField(blank=True, null=True, verbose_name="content")),
                ("tldr", tinymce.models.HTMLField(blank=True, null=True, verbose_name="TL;DR")),
                ("view_count", models.IntegerField(default=0, verbose_name="view count")),
                ("published", models.BooleanField(default=False, verbose_name="published")),
                ("pub_date", models.DateTimeField(blank=True, null=True, verbose_name="publish date")),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agents.agent",
                        verbose_name="author",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_set",
                        to="blogs.category",
                        verbose_name="category",
                    ),
                ),
            ],
            options={
                "verbose_name": "blog post",
                "verbose_name_plural": "blog posts",
                "ordering": ["pub_date"],
            },
        ),
    ]
