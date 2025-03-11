from django.shortcuts import render , redirect
from django.utils.translation import get_language
# import message
from django.contrib import messages

# translate
from django.utils.translation import gettext as _
from .models import *




def home(request):
    if request.method == 'POST':
        # get grade , phone 
        grade=request.POST.get('grade')
        phone=request.POST.get('phone')
        if not grade or not phone:
            messages.error(request, _('Please enter your grade and phone number'))
            print("Please enter your grade and phone number")
            return redirect('home:home')
        # put them in session
        request.session['grade'] = grade
        request.session['phone'] = phone
        # redirect to next page 
        return redirect('demo:request')
    
    section_data = StudentSection.objects.first()
    
    context = {
        'hero': HeroSection.objects.first(),  # Assuming you want only one hero section
        'stats': Statistics.objects.first(),   # Assuming you want only one statistics section
        'categories': CourseCategory.objects.all(),
        'student_testimonials': StudentTestimonial.objects.all(),
        'parent_testimonials': ParentTestimonial.objects.all(),
        'plans': Plans.objects.all(),
        'faqs': Faq.objects.all(),
        'about_section': HomeAboutContent.objects.prefetch_related('features', 'stats').first(),
        'accreditation_section': AccreditationSection.objects.prefetch_related('logos').first(),
        'curriculum_section': CurriculumSection.objects.first(),
        'student_section': section_data,
        'hero_section2': HeroSection2.objects.first()
    }
    
    
    return render(request, 'index.html', context)




