from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from gojjo_realty.blogs.models import Post, Category, BlogMeta

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'created_date', 'modified_date']
    list_filter = ['created_date', 'modified_date']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'description')
        }),
    )
    readonly_fields = ['created_date', 'modified_date']
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'pub_date', 'created_date', 'modified_date']
    list_filter = ['category', 'published', 'created_date', 'modified_date']
    search_fields = ['title', 'subtitle', 'content']
    fieldsets = (
        (None, {
            'fields': ('author', 'category', 'published')
        }),
        ('Post Information', {
            'fields': ('title', 'subtitle', 'image', 'content', 'tldr', 'pub_date')
        }),
    )
    readonly_fields = ['created_date', 'modified_date']
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True
    autocomplete_fields = ['author',]

@admin.register(BlogMeta)
class BlogMetaAdmin(admin.ModelAdmin):
    list_display = ['blog_name', 'subtitle', 'created_date', 'modified_date']
    list_filter = ['created_date', 'modified_date']
    search_fields = ['blog_name', 'subtitle', 'description']
    fieldsets = (
        ('Blog Information', {
            'fields': ('blog_name', 'subtitle', 'header_image', 'description')
        }),
    )
    readonly_fields = ['created_date', 'modified_date']
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True