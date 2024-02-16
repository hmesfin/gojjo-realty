from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from tinymce.models import HTMLField
from django.utils.text import slugify

from gojjo_realty.agents.models import Agent

from gojjo_realty.utils.choices import (
    LINK_CATEGORY_CHOICES,
    LEGAL_DOCUMENT_CHOICES,
    SUBJECT_CHOICES,
    PAGE_TYPE_CHOICES,
    CLIENT_TYPE_CHOICES,
)

class BasePagesModel(models.Model):
    created_date = models.DateTimeField(_('created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True

class ContactMessage(BasePagesModel):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    email = models.EmailField(_('email'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255)
    subject = models.CharField(_('subject'), max_length=255, choices=SUBJECT_CHOICES)
    message = models.TextField(_('message'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('contact message')
        verbose_name_plural = _('contact messages')
        ordering = ['-created_date']


class SiteInfo(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    short_name = models.CharField(_('short name'), max_length=255, blank=True)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    tagline = models.CharField(_('tagline'), max_length=255)
    site_description = models.TextField(_('site description'), blank=True, null=True)
    logo = models.ImageField(_('logo'), upload_to='site/uploads/')
    dark_logo = models.ImageField(_('dark logo'), upload_to='site/uploads/', blank=True, null=True)
    admin_logo = models.ImageField(_('admin logo'), upload_to='site/uploads/', blank=True, null=True)
    favicon = models.ImageField(_('favicon'), upload_to='site/uploads/')
    admin_favicon = models.ImageField(_('admin favicon'), upload_to='site/uploads/', blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    def get_site_name(self):
        return self.name

    class Meta:
        verbose_name = _('site info')
        verbose_name_plural = _('site info')

class HomePage(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    hero_title = models.CharField(_('hero title'), max_length=255)
    hero_subtitle = models.CharField(_('hero subtitle'), max_length=255)
    hero_text = models.TextField(_('hero text'), blank=True, null=True)
    hero_image = models.ImageField(_('hero image'), upload_to='home/uploads/')
    hero_video_url = models.URLField(_('hero video url'), blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('home page')
        verbose_name_plural = _('home pages')
        ordering = ['-created_date']


class AboutPage(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    header_text = models.TextField(_('header text'), max_length=255, blank=True, null=True)
    subtitle = models.TextField(_('subtitle'), max_length=255, blank=True, null=True)
    about_us = HTMLField(_('about us'), blank=True, null=True)
    our_whys = HTMLField(_('our whys'), blank=True, null=True)
    our_commitments = HTMLField(_('our commitments'), blank=True, null=True)
    about_header_image = models.ImageField(_('about header image'), upload_to='about/uploads/', blank=True, null=True)
    about_header_image2 = models.ImageField(_('about side image'), upload_to='about/uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('about page')
        verbose_name_plural = _('about pages')
        ordering = ['-created_date']

class ContactPage(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    contact_cta = models.TextField(_('contact cta'), max_length=255, blank=True, null=True)
    contact_image = models.ImageField(_('contact image'), upload_to='contact/uploads/')
    primary_email = models.EmailField(_('primary email'), max_length=255)
    support_email = models.EmailField(_('support email'), max_length=255, blank=True, null=True)
    compliance_email = models.EmailField(_('compliance email'), max_length=255, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=255)
    fax = models.CharField(_('fax'), max_length=255, blank=True, null=True)
    address = models.TextField(_('address'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('contact page')
        verbose_name_plural = _('contact pages')
        ordering = ['-created_date']

class BusinessSocial(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    tiktok = models.URLField(_('tiktok'), blank=True, null=True)
    facebook = models.URLField(_('facebook'), blank=True, null=True)
    twitter = models.URLField(_('twitter'), blank=True, null=True)
    instagram = models.URLField(_('instagram'), blank=True, null=True)
    youtube = models.URLField(_('youtube'), blank=True, null=True)
    linkedin = models.URLField(_('linkedin'), blank=True, null=True)
    pinterest = models.URLField(_('pinterest'), blank=True, null=True)
    google_business = models.URLField(_('google business'), blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('business social')
        verbose_name_plural = _('business socials')
        ordering = ['-created_date']


class Testimonial(BasePagesModel):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name=_('agent'), blank=True, null=True)
    client_type = models.CharField(_('client type'), max_length=255, choices=CLIENT_TYPE_CHOICES)
    client_image = models.ImageField(_('client image'), upload_to='testimonials/uploads/', blank=True, null=True)
    name = models.CharField(_('name'), max_length=255)
    comment = models.TextField(_('comment'))
    review_date = models.DateField(_('review date'), blank=True, null=True)
    is_published = models.BooleanField(_('is published'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')

class ServicesPage(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    page_header = models.CharField(_('page header'), max_length=255, blank=True, null=True)
    page_subheader = models.TextField(_('page subheader'), max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('services page')
        verbose_name_plural = _('services pages')
        ordering = ['-created_date']

class Service(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255, blank=True, null=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='services/uploads/', blank=True, null=True)
    service_icon = models.CharField(_('service icon'), max_length=255, blank=True, null=True)
    full_description = HTMLField(_('full description'), blank=True, null=True)
    is_published = models.BooleanField(_('is published'), default=True)

    def __str__(self):
        return self.name
    
    def make_slug(self):
        return slugify(self.name)
    
    def save(self, *args, **kwargs):
        self.slug = self.make_slug()
        super(Service, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ['-created_date']


class CallToAction(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=255, choices=PAGE_TYPE_CHOICES)
    title = models.CharField(_('title'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255, blank=True, null=True)
    text = models.TextField(_('text'))
    button_text = models.CharField(_('button text'), max_length=255, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='call-to-action/uploads/', blank=True, null=True)
    video = models.FileField(_('video'), upload_to='call-to-action/uploads/', blank=True, null=True)
    is_published = models.BooleanField(_('is published'), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('call to action')
        verbose_name_plural = _('call to actions')
        ordering = ['-created_date']


class FAQCategory(BasePagesModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    def make_slug(self):
        return self.name.replace(' ', '-')
    
    def save(self, *args, **kwargs):
        self.slug = self.make_slug()
        super(FAQCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('faq category')
        verbose_name_plural = _('faq categories')
        ordering = ['-created_date']

class FAQ(BasePagesModel):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, verbose_name=_('category'))
    question = models.CharField(_('question'), max_length=255)
    answer = models.TextField(_('answer'))
    is_published = models.BooleanField(_('is published'), default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('faq')
        verbose_name_plural = _('faqs')
        ordering = ['-created_date']



class Links(BasePagesModel):
    link_type = models.CharField(_('link type'), max_length=255, choices=LINK_CATEGORY_CHOICES)
    name = models.CharField(_('name'), max_length=255)
    url = models.URLField(_('url'))
    is_published = models.BooleanField(_('is published'), default=True)
    footer_link = models.BooleanField(_('add footer link'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        ordering = ['-created_date']


class Legal(BasePagesModel):
    document_type = models.CharField(_('document type'), max_length=255, choices=LEGAL_DOCUMENT_CHOICES)
    name = models.CharField(_('name'), max_length=255)
    text = HTMLField(_('text'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('legal')
        verbose_name_plural = _('legals')
        ordering = ['-created_date']