from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import *
from modeltranslation.admin import TranslationAdmin

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
    
    
    
    


class FeatureInline(admin.TabularInline):
    model = HomeFeatureItem
    extra = 1
    fields = ('feature_title', 'feature_text', 'icon_class')

class StatisticInline(admin.TabularInline):
    model = HomeStatisticItem
    extra = 1
    fields = ('stat_number', 'stat_label', 'stat_icon')

@admin.register(HomeAboutContent)
class HomeAboutAdmin(TranslationAdmin):
    inlines = [FeatureInline, StatisticInline]
    list_display = ('section_title', 'subtitle')
    fieldsets = (
        (None, {
            'fields': ('section_title', 'subtitle', 'main_description', 'banner_image', 'button_label')
        }),
    )
    
   
   
class AccreditationLogoInline(admin.TabularInline):
    model = AccreditationLogo
    extra = 1
    fields = ('logo_image', 'logo_url', 'display_order')
    sortable_field_name = "display_order"

@admin.register(AccreditationSection)
class AccreditationAdmin(TranslationAdmin):
    inlines = [AccreditationLogoInline]
    list_display = ('main_title_part1', 'highlighted_word')
    
    fieldsets = (
        ('Titles', {
            'fields': (
                ('section_subtitle',),
                ('main_title_part1', 'highlighted_word', 'main_title_part2')
            )
        }),
    ) 
    
    
    
    
    
    
@admin.register(CurriculumSection)
class CurriculumSectionAdmin(TranslationAdmin):
    list_display = ('main_title_part1', 'highlighted_word')
    
    fieldsets = (
        ('Content', {
            'fields': (
                'section_subtitle',
                ('main_title_part1', 'highlighted_word', 'main_title_part2')
            )
        }),
    )
    
    
from django import forms
from ckeditor.widgets import CKEditorWidget

class StudentSectionForm(forms.ModelForm):
    class Meta:
        model = StudentSection
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(config_name='title_config'),
            'description': CKEditorWidget(),
        }

@admin.register(StudentSection)
class StudentSectionAdmin(admin.ModelAdmin):
    form = StudentSectionForm
    list_display = ('title',)
    
    
    
class HeroSection2Form(forms.ModelForm):
    class Meta:
        model = HeroSection2
        fields = '__all__'
        widgets = {
            'title': CKEditorWidget(),
            'description': CKEditorWidget(),
        }

@admin.register(HeroSection2)
class HeroSection2Admin(admin.ModelAdmin):
    form = HeroSection2Form
    list_display = ('title',)
    