from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import AdminSite
from gojjo_realty.pages.models import (
    ContactMessage,
    SiteInfo,
    Links,
    Legal,
    HomePage,
    Service,
    CallToAction,
    Testimonial,
    BusinessSocial,
    ContactPage,
    AboutPage,
    FAQ,
    FAQCategory,
    ContactPage,
    ServicesPage,
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
    search_fields = ('email', 'subject', 'message', 'first_name', 'last_name', 'phone')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Contact Message'), {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'subject', 'message')
        }),
        (_('Date Information'), {
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('contact message')
        verbose_name_plural = _('contact messages')
        ordering = ['-created_date']

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_date', 'modified_date')
    search_fields = ('name', 'tagline')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Site Info'), {
            'fields': ('type', 'name', 'short_name', 'tagline', 'logo', 'dark_logo', 'admin_logo', 'favicon', 'admin_favicon')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('site info')
        verbose_name_plural = _('site infos')
        ordering = ['-created_date']

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link_type', 'created_date')
    search_fields = ('name', 'category')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Links'), {
            'fields': ('name', 'link_type', 'url', 'is_published')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        ordering = ['-created_date']

@admin.register(Legal)
class LegalAdmin(admin.ModelAdmin):
    list_display = ('name', 'document_type', 'created_date')
    search_fields = ('name', 'document_type')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Legal'), {
            'fields': ('name', 'document_type', 'content')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('legal')
        verbose_name_plural = _('legals')
        ordering = ['-created_date']

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'hero_title', 'created_date')
    search_fields = ('name', 'hero_title', 'hero_subtitle')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Home Page'), {
            'fields': ('type', 'name', 'hero_title', 'hero_subtitle', 'hero_text', 'hero_image', 'hero_video_url')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('home page')
        verbose_name_plural = _('home pages')
        ordering = ['-created_date']

@admin.register(ServicesPage)
class ServicesPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'page_header', 'created_date')
    search_fields = ('name', 'page_header', 'created_date')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Services Page'), {
            'fields': ('name', 'type', 'page_header', 'page_subheader')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('services page')
        verbose_name_plural = _('services pages')
        ordering = ['-created_date']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle', 'created_date')
    search_fields = ('name', 'content')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Service'), {
            'fields': ('name', 'subtitle', 'description', 'long_description', 'image', 'service_icon',  'is_published')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ['-created_date']


@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'title', 'subtitle', 'is_published', 'created_date')
    search_fields = ('name', 'title', 'subtitle', 'text')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (_('Call To Action'), {
            'fields': ('name', 'type', 'title', 'subtitle', 'text', 'button_text', 'image', 'video', 'is_published',)
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date', 'modified_date')
        })
    )
    class Meta:
        verbose_name = _('call to action')
        verbose_name_plural = _('call to actions')
        ordering = ['-created_date']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_type', 'is_published', 'created_date')
    search_fields = ('name', 'comment')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('Testimonial'), {
            'fields': ( 'agent', 'client_type', 'client_image', 'name', 'comment', 'review_date', 'is_published',)
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')
        ordering = ['-created_date']

@admin.register(BusinessSocial)
class BusinessSocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_date')
    search_fields = ('name',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('Business Social'), {
            'fields': ('name', 'type', 'tiktok', 'facebook', 'instagram', 'twitter', 'youtube', 'linkedin', 'pinterest', 'google_business')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('business social')
        verbose_name_plural = _('business socials')
        ordering = ['-created_date']

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'primary_email', 'phone', 'created_date')
    search_fields = ('name', 'primary_email', 'phone', 'address')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('Contact Page'), {
            'fields': ('name', 'type', 'contact_image', 'primary_email', 'support_email', 'compliance_email', 'phone', 'fax', 'address')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('contact page')
        verbose_name_plural = _('contact pages')
        ordering = ['-created_date']


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'created_date')
    search_fields = ('name', 'title', 'about', 'whys')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('About Page'), {
            'fields': ('name', 'type', 'about', 'header_text', 'subtitle', 'whys', 'commitments', 'about_header_image', 'about_header_image2')
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('about page')
        verbose_name_plural = _('about pages')
        ordering = ['-created_date']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_published', 'created_date')
    search_fields = ('question', 'answer')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('FAQ'), {
            'fields': ('category', 'question', 'answer', 'is_published',)
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('faq')
        verbose_name_plural = _('faqs')
        ordering = ['-created_date']

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    search_fields = ('name',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    readonly_fields = ('modified_date', 'created_date')

    fieldsets = (
        (_('FAQ Category'), {
            'fields': ('name',)
        }),
        (_('Date Information'), {
            'classes': ('collapse',),
            'fields': ('created_date','modified_date')
        })
    )

    class Meta:
        verbose_name = _('faq category')
        verbose_name_plural = _('faq categories')
        ordering = ['-created_date']