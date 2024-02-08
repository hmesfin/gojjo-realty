# Generated by Django 4.2.9 on 2024-02-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0009_homepage_hero_video_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactmessage",
            name="subject",
            field=models.CharField(
                choices=[
                    ("buying", "Buying"),
                    ("selling", "Selling"),
                    ("investing", "Investing"),
                    ("general_question", "General Question"),
                    ("partnership", "Partnership"),
                    ("other", "Other"),
                ],
                max_length=255,
                verbose_name="subject",
            ),
        ),
    ]