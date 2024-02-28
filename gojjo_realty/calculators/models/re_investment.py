from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from gojjo_realty.utils.models import TimeStampedModel

from gojjo_realty.utils.choices import (
    PROPERTY_TYPE_CHOICES,
    STATE_CHOICES
    )

class Property(TimeStampedModel):
    property_name = models.CharField(max_length=255, verbose_name=_('Property Name'))
    property_type = models.CharField(max_length=255, verbose_name=_('Property Type'), choices=PROPERTY_TYPE_CHOICES)
    property_address = models.CharField(max_length=255, verbose_name=_('Property Address'), blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name=_('City'), blank=True, null=True)
    state = models.CharField(max_length=255, verbose_name=_('State'), choices=STATE_CHOICES, blank=True, null=True)
    zip_code = models.CharField(max_length=255, verbose_name=_('Zip Code'), blank=True, null=True)
    property_description = models.TextField(verbose_name=_('Property Description'), blank=True, null=True)
    property_image = models.ImageField(upload_to='property_images', verbose_name=_('Property Image'), blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Sale Price'), blank=True, null=True)
    rental_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Rental Income'), blank=True, null=True)
    operating_expenses = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Operating Expense'), blank=True, null=True)

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.property_name
    
    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])
    

class Financing(TimeStampedModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='financing', verbose_name=_('Property'))
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Purchase Price'))
    down_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Down Payment'), default=20)
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Interest Rate'), default=6.5)
    loan_term = models.IntegerField(verbose_name=_('Loan Term'), default=30)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Loan Amount'), blank=True, null=True)

    class Meta:
        verbose_name = _('Financing')
        verbose_name_plural = _('Financings')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.property.property_name
    
    def get_absolute_url(self):
        return reverse('financing_detail', args=[str(self.id)])