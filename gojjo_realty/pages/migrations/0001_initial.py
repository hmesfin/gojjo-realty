# Generated by Django 4.2.9 on 2024-02-01 16:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("agents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("about", ckeditor.fields.RichTextField(verbose_name="about")),
                ("whys", ckeditor.fields.RichTextField(verbose_name="our whys")),
                ("commitments", ckeditor.fields.RichTextField(verbose_name="our commitments")),
                (
                    "about_header_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="about/uploads/", verbose_name="about header image"
                    ),
                ),
                (
                    "about_header_image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="about/uploads/", verbose_name="about side image"
                    ),
                ),
            ],
            options={
                "verbose_name": "about page",
                "verbose_name_plural": "about pages",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="BusinessSocial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("tiktok", models.URLField(blank=True, null=True, verbose_name="tiktok")),
                ("facebook", models.URLField(blank=True, null=True, verbose_name="facebook")),
                ("twitter", models.URLField(blank=True, null=True, verbose_name="twitter")),
                ("instagram", models.URLField(blank=True, null=True, verbose_name="instagram")),
                ("youtube", models.URLField(blank=True, null=True, verbose_name="youtube")),
                ("linkedin", models.URLField(blank=True, null=True, verbose_name="linkedin")),
                ("pinterest", models.URLField(blank=True, null=True, verbose_name="pinterest")),
                ("google_business", models.URLField(blank=True, null=True, verbose_name="google business")),
            ],
            options={
                "verbose_name": "business social",
                "verbose_name_plural": "business socials",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="CallToAction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("subtitle", models.CharField(max_length=255, verbose_name="subtitle")),
                ("text", models.TextField(verbose_name="text")),
                ("button_text", models.CharField(max_length=255, verbose_name="button text")),
                ("button_url", models.URLField(verbose_name="button url")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="call-to-action/uploads/", verbose_name="image"
                    ),
                ),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="call-to-action/uploads/", verbose_name="video"),
                ),
                ("is_published", models.BooleanField(default=True, verbose_name="is published")),
            ],
            options={
                "verbose_name": "call to action",
                "verbose_name_plural": "call to actions",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("first_name", models.CharField(max_length=255, verbose_name="first name")),
                ("last_name", models.CharField(max_length=255, verbose_name="last name")),
                ("email", models.EmailField(max_length=255, verbose_name="email")),
                ("phone", models.CharField(max_length=255, verbose_name="phone")),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("buying", "Buying"),
                            ("selling", "Selling"),
                            ("investing", "Investing"),
                            ("general_question", "General Question"),
                            ("partnership", "partnership"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="subject",
                    ),
                ),
                ("message", models.TextField(verbose_name="message")),
            ],
            options={
                "verbose_name": "contact message",
                "verbose_name_plural": "contact messages",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="ContactPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("contact_image", models.ImageField(upload_to="contact/uploads/", verbose_name="contact image")),
                ("primary_email", models.EmailField(max_length=255, verbose_name="primary email")),
                (
                    "support_email",
                    models.EmailField(blank=True, max_length=255, null=True, verbose_name="support email"),
                ),
                (
                    "compliance_email",
                    models.EmailField(blank=True, max_length=255, null=True, verbose_name="compliance email"),
                ),
                ("phone", models.CharField(max_length=255, verbose_name="phone")),
                ("fax", models.CharField(blank=True, max_length=255, null=True, verbose_name="fax")),
                ("address", models.TextField(verbose_name="address")),
            ],
            options={
                "verbose_name": "contact page",
                "verbose_name_plural": "contact pages",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="FAQCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("slug", models.SlugField(max_length=255, unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "faq category",
                "verbose_name_plural": "faq categories",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("hero_title", models.CharField(max_length=255, verbose_name="hero title")),
                ("hero_subtitle", models.CharField(max_length=255, verbose_name="hero subtitle")),
                ("hero_text", models.TextField(blank=True, null=True, verbose_name="hero text")),
                ("hero_image", models.ImageField(upload_to="home/uploads/", verbose_name="hero image")),
            ],
            options={
                "verbose_name": "home page",
                "verbose_name_plural": "home pages",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="Legal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("tos", "Terms and Conditions"),
                            ("privacy", "Privacy Policy"),
                            ("disclaimer", "Disclaimer"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="document type",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("content", ckeditor.fields.RichTextField(verbose_name="content")),
            ],
            options={
                "verbose_name": "legal",
                "verbose_name_plural": "legals",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="Links",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "link_type",
                    models.CharField(
                        choices=[
                            ("affiliates", "Affiliates"),
                            ("footer", "Footer"),
                            ("support", "Support"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="link type",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("url", models.URLField(verbose_name="url")),
                ("is_published", models.BooleanField(default=True, verbose_name="is published")),
                ("footer_link", models.BooleanField(default=False, verbose_name="add footer link")),
            ],
            options={
                "verbose_name": "link",
                "verbose_name_plural": "links",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("subtitle", models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle")),
                ("slug", models.SlugField(max_length=255, unique=True, verbose_name="slug")),
                ("description", models.TextField(verbose_name="description")),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="services/uploads/", verbose_name="image"),
                ),
                (
                    "long_description",
                    ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="long description"),
                ),
                ("is_published", models.BooleanField(default=True, verbose_name="is published")),
            ],
            options={
                "verbose_name": "service",
                "verbose_name_plural": "services",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="SiteInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("short_name", models.CharField(blank=True, max_length=255, verbose_name="short name")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("primary", "Primary"),
                            ("secondary", "Secondary"),
                            ("special", "Special"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                ("tagline", models.CharField(max_length=255, verbose_name="tagline")),
                ("logo", models.ImageField(upload_to="site/uploads/", verbose_name="logo")),
                (
                    "dark_logo",
                    models.ImageField(blank=True, null=True, upload_to="site/uploads/", verbose_name="dark logo"),
                ),
                (
                    "admin_logo",
                    models.ImageField(blank=True, null=True, upload_to="site/uploads/", verbose_name="admin logo"),
                ),
                ("favicon", models.ImageField(upload_to="site/uploads/", verbose_name="favicon")),
                (
                    "admin_favicon",
                    models.ImageField(blank=True, null=True, upload_to="site/uploads/", verbose_name="admin favicon"),
                ),
            ],
            options={
                "verbose_name": "site info",
                "verbose_name_plural": "site info",
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "client_type",
                    models.CharField(
                        choices=[
                            ("buyer", "Buyer"),
                            ("seller", "Seller"),
                            ("buyer_seller", "Buyer/Seller"),
                            ("investor", "investor"),
                        ],
                        max_length=255,
                        verbose_name="client type",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("comment", models.TextField(verbose_name="comment")),
                ("review_date", models.DateField(blank=True, null=True, verbose_name="review date")),
                ("is_published", models.BooleanField(default=True, verbose_name="is published")),
                (
                    "agent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agents.agent",
                        verbose_name="agent",
                    ),
                ),
            ],
            options={
                "verbose_name": "testimonial",
                "verbose_name_plural": "testimonials",
            },
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified_date", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("question", models.CharField(max_length=255, verbose_name="question")),
                ("answer", models.TextField(verbose_name="answer")),
                ("is_published", models.BooleanField(default=True, verbose_name="is published")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.faqcategory", verbose_name="category"
                    ),
                ),
            ],
            options={
                "verbose_name": "faq",
                "verbose_name_plural": "faqs",
                "ordering": ["-created_date"],
            },
        ),
    ]
