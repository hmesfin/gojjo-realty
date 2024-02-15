# Generated by Django 4.2.9 on 2024-02-15 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("landingpages", "0003_remove_landingpage_agents_landingpage_agent"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="landing_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="landingpage_contacts",
                to="landingpages.landingpage",
                verbose_name="Landing Page",
            ),
        ),
        migrations.AddField(
            model_name="venue",
            name="landing_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="landingpage_venues",
                to="landingpages.landingpage",
                verbose_name="Landing Page",
            ),
        ),
    ]
