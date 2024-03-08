from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [

    path('', views.dashboard),
    path('amsai/lms/', views.index),
    path('amsai/lms/login/', views.login),
    path('amsai/lms/dashboard/', views.dashboard),
    path('amsai/lms/profile/', views.profile),
    path('amsai/lms/nonstudent_register/', views.registerNonstudent, name='register'),
    path("amsai/lms/logout/", views.logout),

]