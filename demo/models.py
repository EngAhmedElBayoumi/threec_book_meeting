from django.db import models

# Create your models here.
# Create your models here.
days = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)

class working_setting(models.Model):
    day = models.CharField(max_length=10,choices=days)
    start_time = models.TimeField(help_text="time in formate HH:MM like 17:00")
    end_time = models.TimeField(help_text="time in formate HH:MM like 17:00")
    #meeting time duration by hour and minute
    meeting_duration_hour = models.IntegerField(null=True,blank=True)
    meeting_duration_minute = models.IntegerField(null=True,blank=True)
    #break time duration by hour and minute
    break_time_from = models.TimeField()
    break_time_to = models.TimeField()

    def __str__(self):
        return self.day
    
    # on save validate that hour or minute must be filled
    def save(self, *args, **kwargs):
        if self.meeting_duration_hour is None and self.meeting_duration_minute is None:
            raise ValueError('meeting_duration_hour or meeting_duration_minute must be filled')
        super(working_setting, self).save(*args, **kwargs)
    
    

class meeting(models.Model):
    phone=models.CharField(max_length=20)
    grade=models.CharField(max_length=20)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    meeting_url=models.CharField(max_length=5000,null=True,blank=True)

    def __str__(self):
        return str(self.meeting_date)