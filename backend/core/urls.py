import imp
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

#importing views 
from .views import index
from teachers.views import login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user, name="login"),
    path('index', index, name="index"),
    path('teachers/', include('teachers.urls')),
    #Using django in-built authentication
    path('teachers/', include('django.contrib.auth.urls')),
    path('attendance/', include('attendance.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

