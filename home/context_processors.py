
from django.utils.translation import get_language
def language(request):
    context = {
        'LANGUAGE_CODE': get_language(),
    }
    return context

