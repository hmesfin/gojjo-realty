from django.contrib import admin

from gojjo_realty.agents.models import Agent, License, SocialAccount, Address, AgentPage

class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    extra = 1
    min_num = 0
    max_num = 5
    verbose_name = 'Social Account'
    verbose_name_plural = 'Social Accounts'
    can_delete = True
    show_change_link = True
    fields = ('name', 'url', 'is_published')
    classes = ['collapse']

class LicenseInline(admin.TabularInline):
    model = License
    extra = 1
    min_num = 0
    max_num = 3
    verbose_name = 'License'
    verbose_name_plural = 'Licenses'
    can_delete = True
    show_change_link = True
    fields = ('number', 'state', 'type', 'expiration_date', 'is_published')
    classes = ['collapse']

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    min_num = 0
    max_num = 3
    verbose_name = 'Address'
    verbose_name_plural = 'Addresses'
    can_delete = True
    show_change_link = True
    fields = ('address_line_1', 'address_line_2', 'city', 'state', 'zip_code', 'address_type', 'is_published')
    classes = ['collapse']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'is_active', 'created_date', 'modified_date']
    list_filter = ['is_active', 'created_date', 'modified_date']
    search_fields = ['user__first_name', 'user__last_name', 'user__email']
    inlines = [SocialAccountInline, LicenseInline, AddressInline]
    fieldsets = (
        (None, {
            'fields': ('user', 'is_active')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'agent_photo', 'phone', 'gender', 'gender_id', 'role', 'focus_areas', 'agent_bio', 'agent_short_bio')
        }),
        ('Start-End Dates', {
            'fields': ('start_date', 'termination_date',)
        }),
        ('Visibile on Website', {
            'fields': ('is_published',)
        }),
    )
    readonly_fields = ['user', 'created_date', 'modified_date']
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True

@admin.register(AgentPage)
class AgentPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'created_date', 'modified_date']
    list_filter = ['is_published', 'created_date', 'modified_date']
    search_fields = ['title', 'content']
    fieldsets = (
        ('Page Content', {
            'fields': ('title', 'content', 'is_published')
        }),
    )
    readonly_fields = ['created_date', 'modified_date']
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True