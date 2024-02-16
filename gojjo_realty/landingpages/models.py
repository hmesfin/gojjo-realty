from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from gojjo_realty.utils.models import TimeStampedModel
from django.utils.text import slugify

from gojjo_realty.agents.models import Agent

from gojjo_realty.utils.choices import (
    STATE_CHOICES,
    EVENT_ATTENDANCE_CHOICES,
    EVENT_STATUS_CHOICES,
    EVENT_TYPE_CHOICES,
)


class Venue(TimeStampedModel):
    landing_page = models.ForeignKey('LandingPage', on_delete=models.CASCADE, verbose_name=_('Event'), related_name='landingpage_venues', blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    address = models.CharField(max_length=255, verbose_name=_('Address'))
    city = models.CharField(max_length=255, verbose_name=_('City'))
    state = models.CharField(max_length=255, verbose_name=_('State'), choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=255, verbose_name=_('Zip Code'))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))
    website = models.URLField(verbose_name=_('Website'))
    email = models.EmailField(verbose_name=_('Email'))

    class Meta:
        verbose_name = _('Venue')
        verbose_name_plural = _('Venues')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landingpages:venue', kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Contact(TimeStampedModel):
    landing_page = models.ForeignKey('LandingPage', on_delete=models.CASCADE, verbose_name=_('Landing Page'), related_name='landingpage_contacts', blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))
    message = models.TextField(verbose_name=_('Message'), blank=True, null=True)
    attending = models.CharField(max_length=255, verbose_name=_('Attending'), choices=EVENT_ATTENDANCE_CHOICES, default='yes')

    class Meta:
        verbose_name = _('Ateendee')
        verbose_name_plural = _('Atendees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('landingpages:contact', kwargs={'slug': self.slug})


class LandingPage(TimeStampedModel):
    type = models.CharField(max_length=255, verbose_name=_('Type'), choices=EVENT_TYPE_CHOICES, blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name=_('Title'), unique=True)
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    content = models.TextField(verbose_name=_('Content'))
    featured_image = models.ImageField(upload_to='landingpages', verbose_name=_('Featured Image'), blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Organizer'), related_name='landing_pages')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, verbose_name=_('Venue'), related_name='landing_pages', blank=True, null=True)
    date = models.DateTimeField(verbose_name=_('Date'), blank=True, null=True)
    start_time = models.TimeField(verbose_name=_('Start Time'), blank=True, null=True)
    end_time = models.TimeField(verbose_name=_('End Time'), blank=True, null=True)
    contacts = models.ManyToManyField(Contact, blank=True, verbose_name=_('Contacts'), related_name='landing_pages')
    status = models.CharField(max_length=255, verbose_name=_('Status'), choices=EVENT_STATUS_CHOICES, default='draft')
    online_event = models.BooleanField(default=False, verbose_name=_('Online Event'))
    event_link = models.URLField(verbose_name=_('Event Link'), blank=True, null=True)
    faqs = models.ManyToManyField('EventFAQ', blank=True, verbose_name=_('FAQs'), related_name='landing_pages')

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug})
    
    def get_venue_name(self):
        if self.venue:
            return self.venue.name
        return ''
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class EventFAQ(TimeStampedModel):
    landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE, verbose_name=_('Event'), related_name='event_faqs')
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))
    is_published = models.BooleanField(default=True, verbose_name=_('Published'))

    class Meta:
        verbose_name = _('Event FAQ')
        verbose_name_plural = _('Event FAQs')

    def __str__(self):
        return self.question

