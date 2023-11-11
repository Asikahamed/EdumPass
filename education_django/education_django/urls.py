from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/courses/', include('course.urls')),
    path('api/v1/activities/', include('activity.urls')),
    path('api/v1/projects/', include('project.urls')),
    path('api/v1/contact/', views.submit_contact, name='contact-form')


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)