from django.contrib import admin 
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include 
# import settings , static
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = (
    [
        path("i18n/", include("django.conf.urls.i18n")),
    ]
    + i18n_patterns(
        path("admin/", admin.site.urls),
        path('', include('home.urls')), 
        path('', include('demo.urls')), 
        path('set_language/', include('django.conf.urls.i18n')),
    )
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

