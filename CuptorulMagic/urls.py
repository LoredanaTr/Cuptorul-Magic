from django.urls import path, include
from django.conf.urls.static import static
from CuptorulMagic import settings
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_CuptorulMagic.urls')),
    path('', include('account.urls')),
    path('', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
