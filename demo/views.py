from django.shortcuts import render , redirect
from django.http import JsonResponse
from .models import meeting, working_setting
from datetime import datetime, timedelta
import pytz
from django.contrib import messages
from django.utils.translation import gettext as _
import json
from django.conf import settings
import requests
import jwt
import time
from twilio.rest import Client
import base64
from zoomus import ZoomClient

# Create your views here.

def request_demo(request):
    # check that phone , grade in session is not null
    if 'phone' not in request.session or 'grade' not in request.session:
        messages.error(request, _('Please enter your grade and phone number'))
        return redirect('home:home')
    return render(request, 'bookzoom.html')


def get_available_time(request):
    # Get day name and date from the request
    day_name = request.GET.get("dayName")
    date = request.GET.get("date")

    # Get available time for the team
    available_time = get_available_time_for_team(day_name, date)
    
    # Check if the requested date is tomorrow
    today = datetime.today().strftime("%Y-%m-%d")
    tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    if date == tomorrow:
        # Set the timezone for Houston
        houston_timezone = pytz.timezone('America/Chicago')
        current_time = datetime.now(houston_timezone).strftime("%H:%M")
        # Remove time slots earlier than the current time + 2 hours
        available_time = [
            time_slot for time_slot in available_time 
            if time_slot['from'] > current_time
        ]
    
    # Return the available times as a JSON response
    return JsonResponse({'available_times': available_time})

def get_available_time_for_team(day_name, date):
    # Fetch the working day settings for the given day name
    working_day = working_setting.objects.filter(day=day_name).first()
    if not working_day:
        return []

    # Get relevant time and meeting details from the settings
    start_time = working_day.start_time
    end_time = working_day.end_time
    meeting_duration_hour = working_day.meeting_duration_hour or 0
    meeting_duration_minute = working_day.meeting_duration_minute or 0
    break_time_from = working_day.break_time_from
    break_time_to = working_day.break_time_to

    # Calculate the available time slots
    working_time = calculate_available_time(
        start_time, end_time, meeting_duration_hour, 
        meeting_duration_minute, break_time_from, break_time_to
    )

    # Parse the requested date
    meeting_date = datetime.strptime(date, "%Y-%m-%d").date()

    # Remove reserved time slots
    available_time = remove_reserved_times(working_time, meeting_date)

    return available_time

def calculate_available_time(start_time, end_time, meeting_duration_hour, meeting_duration_minute, break_time_from, break_time_to):
    available_times = []
    current_time = start_time
    duration = timedelta(hours=meeting_duration_hour, minutes=meeting_duration_minute)

    while current_time < end_time:
        next_time = (datetime.combine(datetime.today(), current_time) + duration).time()

        # Check if the current time slot overlaps with the break time
        if not (break_time_from <= current_time < break_time_to) and not (break_time_from < next_time <= break_time_to):
            available_times.append({
                "from": current_time.strftime("%H:%M"),
                "to": next_time.strftime("%H:%M")
            })

        current_time = next_time

    return available_times

def remove_reserved_times(available_times, meeting_date):
    # Fetch all reserved meetings for the given date
    reserved_meetings = meeting.objects.filter(meeting_date=meeting_date)
    reserved_times = {(m.start_time, m.end_time) for m in reserved_meetings}

    # Filter out available time slots that overlap with reserved times
    filtered_times = []
    for time_slot in available_times:
        start_time = datetime.strptime(time_slot['from'], "%H:%M").time()
        end_time = datetime.strptime(time_slot['to'], "%H:%M").time()

        overlap = any(
            reserved_start < end_time and reserved_end > start_time
            for reserved_start, reserved_end in reserved_times
        )

        if not overlap:
            filtered_times.append(time_slot)

    return filtered_times




# def booking(request):
#     if request.method == 'POST':
#         # Get the form data
#         meeting_date = request.POST.get('date')
#         from_time = request.POST.get('from_time')
#         to_time = request.POST.get('to_time')
#         phone=request.session['phone']
#         grade=request.session['grade']
#         # Create a new meeting
#         meeting.objects.create(
#             meeting_date=meeting_date,
#             start_time=from_time,
#             end_time=to_time,
#             phone=phone,
#             grade=grade
#         )
#         # clear the session
#         del request.session['phone']
#         del request.session['grade']
        
    
        
#         messages.success(request, _('Booking success!'))
#         return redirect('home:home')

#     return redirect('home:home')


def create_zoom_meeting(start_time, duration, topic):
    # Create a Zoom client
    client = ZoomClient(settings.ZOOM_API_KEY, settings.ZOOM_API_SECRET, settings.ZOOM_ACCOUNT_ID)

    # Check if start_time is a string and convert it to a datetime object
        
    # Create a Zoom meeting
    meeting_info = client.meeting.create(user_id='me',
                                         topic=topic,
                                         type=2,  
                                         start_time=datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ'),
                                         duration=duration,
                                         timezone='UTC',
                                         settings={
                                            "host_video": True,
                                            "participant_video": True,
                                            "cn_meeting": False,
                                            "in_meeting": False,
                                            "join_before_host": False,
                                            "mute_upon_entry": False,
                                            "watermark": False,
                                            "use_pmi": False,
                                            "approval_type": 0,
                                            "registration_type": 2,
                                            "audio": "both",
                                            "auto_recording": "none",
                                            "enforce_login": False,
                                            "enforce_login_domains": "",
                                            "alternative_hosts": "",
                                            "close_registration": False,
                                            "registrants_confirmation_email": True,
                                            "waiting_room": True,
                                            "global_dial_in_countries": [],
                                            "global_dial_in_numbers": [],
                                            "contact_name": "",
                                            "contact_email": "",
                                            "registrants_email_notification": True,
                                            "meeting_authentication": False
                                        }
                                        
                                        
                                         )
        


    #meeting url
    meeting_info = meeting_info.json()
    print('meeting_info', meeting_info)
    meeting_url=meeting_info.get('join_url')
    return meeting_url


from twilio.rest import Client
from django.conf import settings

def send_to_whatsapp(phone, meeting_url):
    """
    Send a WhatsApp message with the meeting details (date, time, and URL).
    """
    # Twilio credentials
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    from_whatsapp_number = settings.TWILIO_WHATSAPP_FROM

    # Twilio Client
    client = Client(account_sid, auth_token)

    # Pre-approved template SID from Twilio
    content_sid = "HXb5b62575e6e4ff6129ad7c8efe1f983e"  # Replace with your Content SID

    # Content variables for the placeholders in the template
   
    try:
        # Send the WhatsApp message
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"Meeting details:\nURL: {meeting_url}",
            to='whatsapp:2'+phone,
            )

        print(f"WhatsApp message sent successfully! SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
        return None



def booking(request):
    if request.method == 'POST':
        try:
            # Get the form data
            meeting_date = request.POST.get('date')
            from_time = request.POST.get('from_time')
            to_time = request.POST.get('to_time')
            phone = request.session['phone']
            grade = request.session['grade']
            
            duration = int((datetime.strptime(to_time, "%H:%M") - datetime.strptime(from_time, "%H:%M")).total_seconds() / 60)
            zoom_meeting = create_zoom_meeting(meeting_date + "T" + from_time + ":00" + "Z", duration, "zoom meeting demo")
            
            meeting_url=zoom_meeting            
            print("meeting url is \n", meeting_url)
            
            # Create a new meeting in database
            new_meeting = meeting.objects.create(
                meeting_date=meeting_date,
                start_time=from_time,
                end_time=to_time,
                phone=phone,
                grade=grade,
                meeting_url=meeting_url,
            )
            
            
            # sent to whatsapp
            send_to_whatsapp(phone, meeting_url)
        
            # Clear the session
            del request.session['phone']
            del request.session['grade']
            
            messages.success(request, _('Booking successful! Check WhatsApp for meeting details.'))
            
        except Exception as e:
            messages.error(request, _('Booking failed. Please try again.'))
            print(f"Error during booking: {str(e)}")
            
        return redirect('home:home')
    return redirect('home:home')

