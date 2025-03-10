from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import (
    HeroSection, 
    Statistics, 
    CourseCategory, 
    StudentTestimonial,
    ParentTestimonial,
    Plans,
    Faq,
    Feature,
    social
)

# import html formate
from django.utils.html import format_html

from django_json_widget.widgets import JSONEditorWidget
from django import forms


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ['title', 'button_text']
    search_fields = ['title', 'description']

@admin.register(Statistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ['years_experience', 'happy_parents', 'coding_hours', 'graduates']

@admin.register(CourseCategory)
class CourseCategoryAdmin(ModelAdmin):
    list_display = ['name', 'background_color_class', 'icon_preview']
    search_fields = ['name']
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="background-color: black;" />', obj.icon.url)
        return "No Image"
    icon_preview.allow_tags = True
    icon_preview.short_description = 'Icon Preview'


@admin.register(StudentTestimonial)
class StudentTestimonialAdmin(ModelAdmin):
    list_display = ['name', 'video_url']
    search_fields = ['name']


@admin.register(ParentTestimonial)
class ParentTestimonialAdmin(ModelAdmin):
    list_display = ['name', 'image_preview', 'video_url']
    search_fields = ['name']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />',obj.image.url)
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

@admin.register(Plans)
class PlansAdmin(ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name']
    list_filter = ['price']

@admin.register(Faq)
class FaqAdmin(ModelAdmin):
    list_display = ['question', 'answer_preview']
    search_fields = ['question', 'answer']
    
    def answer_preview(self, obj):
        return obj.answer[:100] + '...' if len(obj.answer) > 100 else obj.answer
    answer_preview.short_description = 'Answer Preview'
    
    
@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ['name']
    
    
@admin.register(social)
class socialAdmin(ModelAdmin):
    list_display = ['name']
    
    
    