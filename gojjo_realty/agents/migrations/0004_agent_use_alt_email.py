# Generated by Django 4.2.9 on 2024-02-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agents", "0003_agent_alternate_email_agent_alternate_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="use_alt_email",
            field=models.BooleanField(default=False, verbose_name="Use Alternate Email"),
        ),
    ]