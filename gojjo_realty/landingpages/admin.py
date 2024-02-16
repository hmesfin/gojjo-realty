from django.contrib import admin
from .models import Venue, Contact, LandingPage

class VenueInline(admin.TabularInline):
    model = Venue
    extra = 1
    min_num = 0
    max_num = 1
    verbose_name = 'Venue'
    verbose_name_plural = 'Venues'
    can_delete = True
    show_change_link = True
    fields = ('name', 'address', 'city', 'state', 'zip_code', 'phone', 'website', 'email')
    classes = ['collapse']

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    min_num = 0
    max_num = 1
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
    can_delete = True
    show_change_link = True
    fields = ('first_name', 'last_name', 'email', 'phone', 'message', 'attending')
    classes = ['collapse']

@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ['agent', 'title', 'type', 'status', 'date', 'start_time',]
    search_fields = ['title', 'content']
    list_filter = ['agent', 'type', 'status']
    inlines = [VenueInline, ContactInline]
    fieldsets = (
        (None, {
            'fields': ('agent', 'type', 'title', 'featured_image', 'content', 'status', 'online_event', 'event_link'),
        }),
        ('When', {
            'fields': ('date', 'start_time', 'end_time'),
            'classes': ['collapse'],
        }),
    )