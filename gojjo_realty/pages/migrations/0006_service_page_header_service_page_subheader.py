# Generated by Django 4.2.9 on 2024-02-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_testimonial_client_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="page_header",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="page header"),
        ),
        migrations.AddField(
            model_name="service",
            name="page_subheader",
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name="page subheader"),
        ),
    ]