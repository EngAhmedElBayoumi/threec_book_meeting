from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(HomeAboutContent)
class HomeAboutTranslation(TranslationOptions):
    fields = ('section_title', 'subtitle', 'main_description', 'button_label')

@register(HomeFeatureItem)
class FeatureTranslation(TranslationOptions):
    fields = ('feature_title', 'feature_text')

@register(HomeStatisticItem)
class StatisticTranslation(TranslationOptions):
    fields = ('stat_number', 'stat_label')
    
    
@register(AccreditationSection)
class AccreditationTranslation(TranslationOptions):
    fields = ('section_subtitle', 'main_title_part1', 'highlighted_word', 'main_title_part2')

@register(AccreditationLogo)
class LogoTranslation(TranslationOptions):
    fields = ()
    
    
    
@register(CurriculumSection)
class CurriculumSectionTranslation(TranslationOptions):
    fields = ('section_subtitle', 'main_title_part1', 'highlighted_word', 'main_title_part2')
    
    
@register(StudentSection)
class StudentSectionTranslation(TranslationOptions):
    fields = ('title', 'description')
    
    
    
    
@register(HeroSection2)
class HeroSection2Translation(TranslationOptions):
    fields = ('title', 'description')    
