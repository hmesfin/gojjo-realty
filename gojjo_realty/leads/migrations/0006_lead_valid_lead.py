# Generated by Django 4.2.9 on 2024-02-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0005_alter_lead_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="valid_lead",
            field=models.BooleanField(default=False, verbose_name="Valid Lead"),
        ),
    ]
