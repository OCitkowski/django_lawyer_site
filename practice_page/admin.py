from django.contrib import admin
from .models import OurPracticesAreas, WhyChooseMe


@admin.action(description='Mark selected text as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected text as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


@admin.action(description='Mark selected text as withdrawn')
def make_withdrawn(modeladmin, request, queryset):
    queryset.update(status='w')


class OurPracticesAreasAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_display_links = ('title', 'status')
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"title": ('status',)}


class WhyChooseMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_display_links = ('title', 'status')
    actions = [make_published, make_draft, make_withdrawn]
    prepopulated_fields = {"title": ('status',)}


admin.site.register(OurPracticesAreas, OurPracticesAreasAdmin)
admin.site.register(WhyChooseMe, WhyChooseMeAdmin)
