from .views import request_demo,get_available_time , booking

from django.urls import path

app_name = 'demo'

urlpatterns = [
    path('request/', request_demo, name='request'),
    path('get_available_time/', get_available_time, name='get_available_time'),
    path('booking/', booking, name='booking'),
]