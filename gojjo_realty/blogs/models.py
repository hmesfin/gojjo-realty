from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from gojjo_realty.agents.models import Agent
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from gojjo_realty.utils.openapi import generate_summary


User = get_user_model()

now = timezone.now()


class BlogPostQueryset(models.QuerySet):
 
    def published(self):
        return self.filter(published=True)
 
    def draft(self):
        return self.filter(published=False)


class BaseBlogClass(models.Model):
    created_date = models.DateTimeField(_('created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True

class BlogMeta(BaseBlogClass):
    blog_name = models.CharField(_('blog name'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255, blank=True, null=True)
    header_image = models.ImageField(_('header image'), upload_to='blog/uploads/', blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.blog_name
    
    class Meta:
        verbose_name = _('blog meta')
        verbose_name_plural = _('blog metas')
        ordering = ['-created_date']
    

class Category(BaseBlogClass):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.name
    
    def make_slug(self):
        return slugify(self.name)
    
    def post_count(self):
        return self.post_set.published().count()
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = self.make_slug()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('blog category')
        verbose_name_plural = _('blog categories')
        ordering = ['name']

class Post(BaseBlogClass):
    author = models.ForeignKey(Agent, verbose_name=_('author'), on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE, related_name='post_set')
    title = models.CharField(_('title'), max_length=255)
    subtitle = models.CharField(_('subtitle'), max_length=255, blank=True, null=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    image = models.ImageField(_('header image'), blank=True, null=True, upload_to='blog/uploads/')
    text = RichTextField(_('text'))
    tldr = RichTextField(_('TL;DR'), blank=True, null=True)
    tags = TaggableManager(_('tags'), blank=True)
    view_count = models.IntegerField(_('view count'), default=0)
    published = models.BooleanField(_('published'), default=False)


    pub_date = models.DateTimeField(_('publish date'), blank=True, null=True)

    objects = BlogPostQueryset.as_manager()

    def make_slug(self):
        return slugify(self.title)
    
    def author_name(self):
        if self.author:
            return self.author.get_full_name
        return 'Anonymous'

    def save(self, *args, **kwargs):
        """
        Set publish date to the date when the post's published status is switched to True,
        reset the date if the post is unpublished
        """
        if not self.tldr:
            self.tldr = generate_summary(self.text)
        self.slug = self.make_slug()
        if self.published and self.pub_date is None:
            self.pub_date = datetime.now()
        elif not self.published and self.pub_date is not None:
            self.pub_date = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def new_blog(self):
        return self.pub_date >= now - timedelta(days=7)

    class Meta:
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')
        ordering = ['pub_date']


