# Generated by Django 4.2.9 on 2024-02-01 04:36

import ckeditor.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0002_remove_user_name_user_is_admin_user_is_agent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                ("address_line_1", models.CharField(blank=True, max_length=255, verbose_name="Address Line 1")),
                ("address_line_2", models.CharField(blank=True, max_length=255, verbose_name="Address Line 2")),
                ("city", models.CharField(blank=True, max_length=255, verbose_name="City")),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DE", "Delaware"),
                            ("DC", "District Of Columbia"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinois"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VA", "Virginia"),
                            ("WA", "Washington"),
                            ("WV", "West Virginia"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                            ("AS", "American Samoa"),
                            ("GU", "Guam"),
                            ("MP", "Northern Mariana Islands"),
                            ("PR", "Puerto Rico"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("VI", "Virgin Islands"),
                            ("AA", "Armed Forces Americas"),
                            ("AP", "Armed Forces Pacific"),
                            ("AE", "Armed Forces Others"),
                        ],
                        default="MN",
                        max_length=255,
                        verbose_name="State",
                    ),
                ),
                ("zip_code", models.CharField(blank=True, max_length=255, verbose_name="Zip Code")),
                (
                    "address_type",
                    models.CharField(
                        blank=True,
                        choices=[("home", "Home"), ("office", "Office"), ("mailing", "Mailing"), ("other", "Other")],
                        max_length=255,
                        verbose_name="Address Type",
                    ),
                ),
                ("is_published", models.BooleanField(default=True, verbose_name="Publish")),
            ],
            options={
                "verbose_name": "address",
                "verbose_name_plural": "addresses",
                "ordering": ["city"],
            },
        ),
        migrations.CreateModel(
            name="Agent",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="agent_user",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=255, verbose_name="First Name")),
                ("last_name", models.CharField(blank=True, max_length=255, verbose_name="Last Name")),
                ("slug", models.SlugField(blank=True, max_length=255, verbose_name="Slug")),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None, verbose_name="Phone Number"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("agent", "Agent"),
                            ("broker", "Broker"),
                            ("teamlead", "Team Lead"),
                            ("employee", "Employee"),
                        ],
                        max_length=255,
                        verbose_name="Role",
                    ),
                ),
                ("agent_photo", models.ImageField(blank=True, upload_to="agent_photos", verbose_name="Profile Photo")),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Male"), ("female", "Female"), ("refuse_id", "Refuse to Identify")],
                        max_length=255,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "gender_id",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("he_him", "He/Him"),
                            ("she_her", "She/Her"),
                            ("they_them", "They/Them"),
                            ("refuse_id", "Refuse to Identify"),
                        ],
                        max_length=255,
                        verbose_name="Gender ID",
                    ),
                ),
                ("agent_bio", ckeditor.fields.RichTextField(blank=True, verbose_name="Bio")),
                (
                    "focus_areas",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=255), blank=True, null=True, size=None
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True, verbose_name="Start Date")),
                ("termination_date", models.DateField(blank=True, null=True, verbose_name="Termination Date")),
                ("is_published", models.BooleanField(default=True, verbose_name="Publish")),
                (
                    "addresses",
                    models.ManyToManyField(
                        blank=True, related_name="agent_addresses", to="agents.address", verbose_name="Addresses"
                    ),
                ),
            ],
            options={
                "verbose_name": "agent",
                "verbose_name_plural": "agents",
                "ordering": ["user__email"],
            },
        ),
        migrations.CreateModel(
            name="SocialAccount",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("facebook", "Facebook"),
                            ("twitter", "Twitter"),
                            ("instagram", "Instagram"),
                            ("linkedin", "LinkedIn"),
                            ("pinterest", "Pinterest"),
                            ("youtube", "YouTube"),
                            ("tiktok", "TikTok"),
                        ],
                        max_length=255,
                        verbose_name="Social Account Name",
                    ),
                ),
                ("url", models.URLField(blank=True, max_length=255, verbose_name="Social Account URL")),
                ("is_published", models.BooleanField(default=True, verbose_name="Publish")),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agent_social_account",
                        to="agents.agent",
                        verbose_name="Agent",
                    ),
                ),
            ],
            options={
                "verbose_name": "social account",
                "verbose_name_plural": "social accounts",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="License",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="Modified Date")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                ("number", models.CharField(blank=True, max_length=255, verbose_name="License Number")),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DE", "Delaware"),
                            ("DC", "District Of Columbia"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinois"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VA", "Virginia"),
                            ("WA", "Washington"),
                            ("WV", "West Virginia"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                            ("AS", "American Samoa"),
                            ("GU", "Guam"),
                            ("MP", "Northern Mariana Islands"),
                            ("PR", "Puerto Rico"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("VI", "Virgin Islands"),
                            ("AA", "Armed Forces Americas"),
                            ("AP", "Armed Forces Pacific"),
                            ("AE", "Armed Forces Others"),
                        ],
                        default="MN",
                        max_length=255,
                        verbose_name="License State",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("salesperson", "Salesperson"),
                            ("broker", "Broker"),
                            ("assciate_broker", "Associate Broker"),
                        ],
                        max_length=255,
                        verbose_name="License Type",
                    ),
                ),
                ("expiration_date", models.DateField(blank=True, null=True, verbose_name="License Expiration Date")),
                ("is_published", models.BooleanField(default=True, verbose_name="Publish")),
                (
                    "licensee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="agent_license",
                        to="agents.agent",
                        verbose_name="Licensee",
                    ),
                ),
            ],
            options={
                "verbose_name": "license",
                "verbose_name_plural": "licenses",
                "ordering": ["number"],
            },
        ),
        migrations.AddField(
            model_name="agent",
            name="licenses",
            field=models.ManyToManyField(
                blank=True, related_name="agent_licenses", to="agents.license", verbose_name="Licenses"
            ),
        ),
        migrations.AddField(
            model_name="agent",
            name="social_accounts",
            field=models.ManyToManyField(
                blank=True,
                related_name="agent_social_accounts",
                to="agents.socialaccount",
                verbose_name="Social Accounts",
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="agent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agent_address",
                to="agents.agent",
                verbose_name="Agent",
            ),
        ),
    ]
