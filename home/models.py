from django.db import models


class HeroSection(models.Model):
    title = models.CharField(max_length=200) 
    title_ar = models.CharField(max_length=200, null=True)
    description = models.TextField()  
    description_ar = models.TextField(null=True)
    button_text = models.CharField(max_length=50)  
    button_text_ar = models.CharField(max_length=50, null=True)

    
class Statistics(models.Model):
    years_experience = models.IntegerField()
    happy_parents = models.IntegerField()     
    coding_hours = models.IntegerField()     
    graduates = models.IntegerField() 


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)  
    name_ar = models.CharField(max_length=100, null=True)
    icon = models.ImageField(upload_to='categories/')
    background_color_class = models.CharField(max_length=50)  
    
    
    
class social(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    
class StudentTestimonial(models.Model):
    name = models.CharField(max_length=100) 
    name_ar = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='students/')
    video_url = models.URLField()  # YouTube video URL
    video_url_ar = models.URLField()  # YouTube video URL
    social = models.ManyToManyField(social, related_name='student_testimonials')
    
class ParentTestimonial(models.Model):
    name = models.CharField(max_length=100) 
    name_ar = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='parents/')
    video_url = models.URLField() 
    video_url_ar = models.URLField() 



class Feature(models.Model):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'{self.name}-{self.name_ar}'


class Plans(models.Model):
    name = models.CharField(max_length=100)  # "Basic"
    name_ar = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    description_ar = models.TextField(null=True)
    features = models.ManyToManyField(Feature, related_name='plans')

    
    
    
class Faq(models.Model):
    question = models.CharField(max_length=255)
    question_ar = models.CharField(max_length=255, null=True)
    answer = models.TextField()
    answer_ar = models.TextField(null=True)
    
    

    
     
    

