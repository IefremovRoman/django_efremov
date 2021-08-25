"""django_efremov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    # path('students/', StudentListView.as_view()),
    path('teachers/', list_teachers, name='list-teachers'),
    path('teacher/<int:teacher_id>', get_teacher, name='get-teacher'),
    path('create_teacher', create_teacher, name='create-teacher'),
    path('edit_teacher/<int:teacher_id>', edit_teacher, name='edit-teacher'),
    path('delete_teacher/<int:teacher_id>', delete_teacher, name='delete-teacher'),
    path('generate_teacher/', generate_teacher, name='generate-teacher'),
    path('generate_teacher/<int:qty>', generate_teachers, name='generate-teachers')
]
