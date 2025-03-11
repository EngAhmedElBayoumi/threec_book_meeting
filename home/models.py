from django.db import models
from django.utils.translation import gettext_lazy as _



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
    
    
    
    

class HomeAboutContent(models.Model):
    section_title = models.CharField(_('Section Title'), max_length=200)
    subtitle = models.CharField(_('Subtitle'), max_length=200)
    main_description = models.TextField(_('Main Description'))
    banner_image = models.ImageField(_('Banner Image'), upload_to='about/')
    button_label = models.CharField(_('Button Label'), max_length=50)
    
    class Meta:
        verbose_name = _('Homepage About')
        verbose_name_plural = _('Homepage About Sections')

class HomeFeatureItem(models.Model):
    parent_section = models.ForeignKey(HomeAboutContent, on_delete=models.CASCADE, related_name='features')
    feature_title = models.CharField(_('Feature Title'), max_length=200)
    feature_text = models.TextField(_('Feature Text'))
    icon_class = models.CharField(_('Icon Class'), max_length=50, default='fi fi-ss-check-circle')

    class Meta:
        verbose_name = _('Feature Item')
        verbose_name_plural = _('Feature Items')

class HomeStatisticItem(models.Model):
    parent_section = models.ForeignKey(HomeAboutContent, on_delete=models.CASCADE, related_name='stats')
    stat_number = models.CharField(_('Statistic Number'), max_length=20)
    stat_label = models.CharField(_('Statistic Label'), max_length=100)
    stat_icon = models.FileField(_('Statistic Icon'), upload_to='stats/')

    class Meta:
        verbose_name = _('Statistic Item')
        verbose_name_plural = _('Statistic Items')
    

    
    
class AccreditationSection(models.Model):
    section_subtitle = models.CharField(_('Section Subtitle'), max_length=200)
    main_title_part1 = models.CharField(_('Main Title Part 1'), max_length=100)
    highlighted_word = models.CharField(_('Highlighted Word'), max_length=50)
    main_title_part2 = models.CharField(_('Main Title Part 2'), max_length=100)
    
    class Meta:
        verbose_name = _('Accreditation Section')
        verbose_name_plural = _('Accreditation Sections')

class AccreditationLogo(models.Model):
    parent_section = models.ForeignKey(AccreditationSection, on_delete=models.CASCADE, related_name='logos')
    logo_image = models.FileField(_('Logo Image'), upload_to='accreditations/')
    logo_url = models.URLField(_('Logo URL'), blank=True, null=True)
    display_order = models.PositiveIntegerField(_('Display Order'), default=0)

    class Meta:
        verbose_name = _('Accreditation Logo')
        verbose_name_plural = _('Accreditation Logos')
        ordering = ['display_order']
     
     
     
class CurriculumSection(models.Model):
    section_subtitle = models.CharField(_('Section Subtitle'), max_length=200)
    main_title_part1 = models.CharField(_('Main Title Part 1'), max_length=100)
    highlighted_word = models.CharField(_('Highlighted Word'), max_length=50)
    main_title_part2 = models.CharField(_('Main Title Part 2'), max_length=200)
    
    class Meta:
        verbose_name = _('Curriculum Section')
        verbose_name_plural = _('Curriculum Sections')
        
        
        
from ckeditor.fields import RichTextField

class StudentSection(models.Model):
    title = RichTextField(_('Title'), config_name='title_config')  # حقل العنوان الواحد
    description = RichTextField(_('Description'))
    
    class Meta:
        verbose_name = _('Students Section')
        verbose_name_plural = _('Students Sections')

    

class HeroSection2(models.Model):
    title = RichTextField(_('Title'))
    description = RichTextField(_('Description'))
    main_image = models.ImageField(_('Main Image'), upload_to='hero/')
    background_image = models.ImageField(_('Background Image'), upload_to='hero/bg/')
    
    class Meta:
        verbose_name = _('Hero Section')
        verbose_name_plural = _('Hero Sections')