from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


from gojjo_realty.contacts.choices import (
    ADDRESS_TYPE_CHOICES,
    )


User = get_user_model()

class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        abstract = True

class ContactAddress(BaseTimeStampModel):
    contact = models.ForeignKey('Contact',
                                on_delete=models.CASCADE,
                                related_name='contact_address',
                                verbose_name=_('Contact'))
    address = models.CharField(_('Address'), max_length=255)
    city = models.CharField(_('City'), max_length=100)
    state = models.CharField(_('State'), max_length=100)
    country = models.CharField(_('Country'), max_length=100)
    postal_code = models.CharField(_('Postal Code'), max_length=10)
    address_type = models.CharField(_('Address Type'),
                                    max_length=20,
                                    choices=ADDRESS_TYPE_CHOICES,
                                    default='home')
    current_address = models.BooleanField(_('Current Address'), default=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}"