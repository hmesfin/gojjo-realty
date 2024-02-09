from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from gojjo_realty.users.models import User
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from gojjo_realty.agents.choices import (
    SOCIAL_ACCOUNT_CHOICES,
    STATE_CHOICES,
    LICENSE_TYPE_CHOICES,
    GENDER_CHOICES,
    GENDER_ID_CHOICES,
    ROLE_CHOICES,
    ADDRESS_TYPE_CHOICES,
    )


class BaseAgentModel(models.Model):
    created_date = models.DateTimeField(_("Created Date"), auto_now_add=True)
    modified_date = models.DateTimeField(_("Modified Date"), auto_now=True)
    is_active = models.BooleanField(_("Is Active"), default=True)

    class Meta:
        abstract = True

class AgentPage(BaseAgentModel):
    title = models.CharField(_("Title"), max_length=255, blank=True)
    slug = models.SlugField(_("Slug"), max_length=255, blank=True)
    content = RichTextField(_("Content"), blank=True)
    is_published = models.BooleanField(_("Publish"), default=True)

    class Meta:
        verbose_name = _("agent page")
        verbose_name_plural = _("agent pages")
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
    def make_slug(self):
        return slugify(self.title)
    
    def save(self, *args, **kwargs):
        self.slug = self.make_slug()
        super(AgentPage, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("agents:agent_page_detail", kwargs={"slug": self.slug})

class Address(BaseAgentModel):
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, related_name='agent_address', verbose_name=_("Agent"))
    address_line_1 = models.CharField(_("Address Line 1"), max_length=255, blank=True)
    address_line_2 = models.CharField(_("Address Line 2"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    state = models.CharField(_("State"), max_length=255, blank=True, choices=STATE_CHOICES, default='MN')
    zip_code = models.CharField(_("Zip Code"), max_length=255, blank=True)
    address_type = models.CharField(_("Address Type"), max_length=255, blank=True, choices=ADDRESS_TYPE_CHOICES)
    is_published = models.BooleanField(_("Publish"), default=True)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ['city']
    
    def __str__(self):
        return self.address_line_1
    
class SocialAccount(BaseAgentModel):
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, related_name='agent_social_account', verbose_name=_("Agent"))
    name = models.CharField(_("Social Account Name"), max_length=255, choices=SOCIAL_ACCOUNT_CHOICES)
    url = models.URLField(_("Social Account URL"), max_length=255, blank=True)
    is_published = models.BooleanField(_("Publish"), default=True)

    class Meta:
        verbose_name = _("social account")
        verbose_name_plural = _("social accounts")
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class License(BaseAgentModel):
    licensee = models.ForeignKey('Agent', on_delete=models.CASCADE, related_name='agent_license', verbose_name=_("Licensee"))
    number = models.CharField(_("License Number"), max_length=255, blank=True)
    state = models.CharField(_("License State"), max_length=255, blank=True, choices=STATE_CHOICES, default='MN')
    type = models.CharField(_("License Type"), max_length=255, blank=True, choices=LICENSE_TYPE_CHOICES)
    expiration_date = models.DateField(_("License Expiration Date"), blank=True, null=True)
    is_published = models.BooleanField(_("Publish"), default=True)

    class Meta:
        verbose_name = _("license")
        verbose_name_plural = _("licenses")
        ordering = ['number']
    
    def __str__(self):
        return self.number

class Agent(BaseAgentModel):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='agent_user',
        verbose_name=_("User"),
    )
    first_name = models.CharField(_("First Name"), max_length=255, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True)
    slug = models.SlugField(_("Slug"), max_length=255, blank=True) 
    phone = PhoneNumberField(_("Phone Number"), blank=True)
    role = models.CharField(_("Role"), max_length=255, blank=True, choices=ROLE_CHOICES)
    agent_photo = models.ImageField(_("Profile Photo"), upload_to='agent_photos', blank=True)
    gender = models.CharField(_("Gender"), max_length=255, blank=True, choices=GENDER_CHOICES)
    gender_id = models.CharField(_("Gender ID"), max_length=255, blank=True, choices=GENDER_ID_CHOICES)
    agent_bio = RichTextField(_("Bio"), blank=True)
    agent_short_bio = models.TextField(_("Short Bio"), max_length=255, blank=True)
    social_accounts = models.ManyToManyField(SocialAccount, blank=True, related_name='agent_social_accounts', verbose_name=_("Social Accounts"))
    licenses = models.ManyToManyField(License, blank=True, related_name='agent_licenses', verbose_name=_("Licenses"))
    focus_areas = ArrayField(models.CharField(max_length=255, blank=True), blank=True, null=True,)
    practice_areas = ArrayField(models.CharField(max_length=255, blank=True), blank=True, null=True,)
    addresses = models.ManyToManyField(Address, blank=True, related_name='agent_addresses', verbose_name=_("Addresses"))
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    termination_date = models.DateField(_("Termination Date"), blank=True, null=True)
    is_published = models.BooleanField(_("Publish"), default=False)


    def __str__(self):
        return self.user.email
    
    def get_email(self):
        return self.user.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse("agents:agent_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
    # Update the slug field before saving the model for the first time.
        if not self.slug:
            self.slug = slugify(self.first_name + '-' + self.last_name)
        super().save(*args, **kwargs)  # Save the model instance only once

    
    class Meta:
        verbose_name = _("agent")
        verbose_name_plural = _("agents")
        ordering = ['user__email']
