from django.contrib import admin
from django.urls import path, include
from user import views
from library.models import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.dashboard),
    path('amsai/lms/', views.index),
    path('amsai/lms/login/', views.login),
    path('amsai/lms/dashboard/', views.dashboard),
    path('amsai/lms/profile/', views.profile),
    path('amsai/lms/nonstudent_register/', views.registerNonstudent, name='register'),
    path("amsai/lms/logout/", views.logout),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)