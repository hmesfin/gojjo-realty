from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from gojjo_realty.agents.models import Agent

from django.urls import reverse

from gojjo_realty.utils.choices import (
    PHONE_TYPE_CHOICES,
    CONTACT_RELATIONSHIP_CHOICES,
    CONTACT_GENDER_CHOICES,
    CONTACT_PRONOUN_CHOICES,
    )

User = get_user_model()

class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True

class Relationship(BaseTimeStampModel):
    contact = models.ForeignKey('Contact',
                                on_delete=models.CASCADE,
                                related_name='contact_relationships',
                                verbose_name=_('Contact'))
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    phone_number = PhoneNumberField(_('Phone Number'), unique=True)
    phone_number_type = models.CharField(_('Phone Number Type'), choices=PHONE_TYPE_CHOICES, default='mobile')
    relationship = models.CharField(_('Relationship'),
                                    max_length=10,
                                    choices=CONTACT_RELATIONSHIP_CHOICES,
                                    default='other')
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    anniversary = models.DateField(_('Anniversary'), blank=True, null=True)
    gender = models.CharField(_('Gender'), choices=CONTACT_GENDER_CHOICES, blank=True)
    pronoun = models.CharField(_('Pronoun'), choices=CONTACT_PRONOUN_CHOICES, blank=True)
    is_emergency_contact = models.BooleanField(_('Is Emergency Contact'), default=False)
    is_primary_contact = models.BooleanField(_('Is Primary Contact'), default=False)

    def __str__(self):
        return f"{self.contact} is {self.relationship} to {self.related_contact}"
    
    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'pk': self.contact.pk})
    
    def get_update_url(self):
        return reverse('contacts:contact-update', kwargs={'pk': self.contact.pk})
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        return date.today().year - self.birthday.year