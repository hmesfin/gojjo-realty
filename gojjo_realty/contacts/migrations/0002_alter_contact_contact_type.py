# Generated by Django 4.2.9 on 2024-02-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="contact_type",
            field=models.CharField(
                choices=[("lead", "Lead"), ("client", "Client"), ("vendor", "Vendor"), ("other", "Other")],
                default="client",
                max_length=10,
                verbose_name="Contact Type",
            ),
        ),
    ]
