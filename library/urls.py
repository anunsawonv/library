"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from library import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Books -- NonStudent
    path('amsai/lms/nonstudent/borrowed_books/', views.nonBorrowedBooks),
    path('amsai/lms/nonstudent/returned_books/', views.nonReturnedBooks),

    # Books -- Student
    path('amsai/lms/books/', views.allBooks),
    path('amsai/lms/borrowed_books/', views.myBorrowedBooks),
    path('amsai/lms/returned_books/', views.myReturnedBooks),
    path('amsai/lms/books/<int:nid>/borrow/', views.borrow),

    # Events
    path('amsai/lms/events/', views.Events),
    path('amsai/lms/events/add/', views.addEvents),

    # Announcements
    path('amsai/lms/announcements/', views.Announcement),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
