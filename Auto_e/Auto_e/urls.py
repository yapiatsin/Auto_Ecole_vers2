from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automob_ecole.urls')),
    path('authent/', include('django.contrib.auth.urls')),
    path('authent/', include('authentification.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
