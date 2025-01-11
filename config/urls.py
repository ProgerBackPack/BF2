from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
from services.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_page'),
    path('services/', include('services.urls', namespace='services')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)