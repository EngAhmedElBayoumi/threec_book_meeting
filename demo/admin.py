from django.contrib import admin
from .models import working_setting , meeting
from unfold.admin import ModelAdmin
from django.utils.html import format_html
# Register your models here.

@admin.register(working_setting)
class working_settingAdmin(ModelAdmin):
    list_display = ['day' , 'start_time' , 'end_time','meeting_duration_hour','meeting_duration_minute','break_time_from','break_time_to']
    #search 
    search_fields = ['day' , 'start_time' , 'end_time','meeting_duration_hour','meeting_duration_minute','break_time_from','break_time_to']
    
    
@admin.register(meeting)
class meetingAdmin(ModelAdmin):
    list_display = ['phone' , 'grade' , 'meeting_date','start_time' , 'end_time',"display_url"]
    #search 
    search_fields = ['phone' , 'grade' , 'meeting_date','start_time' , 'end_time']
    def display_url(self , obj):
        url = format_html(
            '<a href="{}" target="_blank" style="color:blue; max-width: 300px; display: block;">{}</a>',
            obj.meeting_url,
            obj.meeting_url
            
        )
        return url
    display_url.short_description = 'Meeting URL'
    
    

    