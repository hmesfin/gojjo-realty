from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from gojjo_realty.agents.models import Agent

from django.urls import reverse

from gojjo_realty.utils.choices import (
    CONTACT_TYPE_CHOICES,
    PHONE_TYPE_CHOICES,
    CONTACT_GENDER_CHOICES,
    CONTACT_PRONOUN_CHOICES,
    CONTACT_PREFERRED_CONTACT_METHOD_CHOICES,
    CONTACT_MARITAL_STATUS_CHOICES,
    )

User = get_user_model()

class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True

class Contact(BaseTimeStampModel):
    agent = models.ForeignKey(Agent,
                              on_delete=models.CASCADE,
                              related_name='contacts',
                              verbose_name=_('Agent'))
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    phone_number = PhoneNumberField(_('Phone Number'), unique=True)
    phone_type = models.CharField(_('Phone Type'),
                                  max_length=10,
                                  choices=PHONE_TYPE_CHOICES,
                                  default='mobile')
    marital_status = models.CharField(_('Marital Status'),
                                    max_length=50,
                                    choices=CONTACT_MARITAL_STATUS_CHOICES,
                                    default='single')
    gender = models.CharField(_('Gender'), choices=CONTACT_GENDER_CHOICES, blank=True)
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True)
    pronoun = models.CharField(_('Pronoun'), choices=CONTACT_PRONOUN_CHOICES, blank=True)
    can_text = models.BooleanField(_('Can Text'), default=True)
    contact_type = models.CharField(_('Contact Type'),
                                    max_length=10,
                                    choices=CONTACT_TYPE_CHOICES,
                                    default='client')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', verbose_name=_('Contact User'))
    can_email = models.BooleanField(_('Can Email'), default=True)
    can_snail_mail = models.BooleanField(_('Can Snail Mail'), default=False)
    preferred_contact_method = models.CharField(_('Preferred Contact Method'),
                                                max_length=20,
                                                choices=CONTACT_PREFERRED_CONTACT_METHOD_CHOICES,
                                                default='email')
    additional_info = models.OneToOneField('ContactAdditionalInfo', on_delete=models.CASCADE, related_name='additonal_info', verbose_name=_('Additional Info'))
    relationships = models.ManyToManyField('Relationship', related_name='relationships', verbose_name=_('Relationships'))
    addresses = models.ManyToManyField('ContactAddress', related_name='addresses', verbose_name=_('Addresses'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('contacts:contact-update', kwargs={'pk': self.pk})
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        return date.today().year - self.birthdate.year
    

