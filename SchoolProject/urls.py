from django.contrib import admin
from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    path('', views.studentApi),  # Default URL (empty string for the homepage)
    path('student', views.studentApi),  # This will match '/student'
    re_path(r'^student/([0-9]+)$', views.studentApi),  # Match student with an ID
    path('admin/', admin.site.urls),
]



