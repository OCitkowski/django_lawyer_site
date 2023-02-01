from django.contrib import admin
from .models import Carousel, ReviewFromClient


@admin.action(description='Mark selected text as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected text as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


@admin.action(description='Mark selected text as withdrawn')
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_display_links = ('title', 'status')
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"title": ('status',)}


class ReviewFromClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'status')
    list_display_links = ('client_name', 'status')
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"client_name": ('status',)}


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(ReviewFromClient, ReviewFromClientAdmin)
