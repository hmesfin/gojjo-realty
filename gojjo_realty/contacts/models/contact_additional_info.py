from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from django.urls import reverse

from gojjo_realty.contacts.choices import (
    CONTACT_EDUCATION_LEVEL_CHOICES,
    CONTACT_EMPLOYMENT_STATUS_CHOICES,
    CONTACT_INCOME_LEVEL_CHOICES,
    )


User = get_user_model()

class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True

class ContactAdditionalInfo(BaseTimeStampModel):
    contact = models.OneToOneField(
        'Contact',
        on_delete=models.CASCADE,
        related_name='contact_additional_info',
        verbose_name=_('Contact'))
    employment_status = models.CharField(_('Employment Status'),
                                        max_length=50,
                                        choices=CONTACT_EMPLOYMENT_STATUS_CHOICES,
                                        default='employed')
    education_level = models.CharField(_('Education Level'),
                                       max_length=50,
                                       choices=CONTACT_EDUCATION_LEVEL_CHOICES,
                                       default='high_school')
    income_level = models.CharField(_('Income Level'),
                                   max_length=50,
                                   choices=CONTACT_INCOME_LEVEL_CHOICES,
                                   default='middle')
    household_income_level = models.CharField(_('Household Income Level'),
                                             max_length=100,
                                             choices=CONTACT_INCOME_LEVEL_CHOICES,
                                             default='middle')
    
    def __str__(self):
        return f"{self.contact} Additional Info"
    
    def get_absolute_url(self):
        return reverse('contacts:contact-detail', kwargs={'pk': self.contact.pk})
    
    def get_update_url(self):
        return reverse('contacts:contact-update', kwargs={'pk': self.contact.pk})