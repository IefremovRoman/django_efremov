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

from .views import (TeacherListView,
                    get_teacher,
                    TeacherCreateView,
                    # create_teacher,
                    edit_teacher,
                    delete_teacher,
                    generate_teacher,
                    generate_teachers)

app_name = 'teachers'
urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='list'),
    # path('teachers/', list_teachers, name='list-teachers'),
    path('teacher/<int:teacher_id>', get_teacher, name='get'),
    # path('create_teacher', create_teacher, name='create'),
    path('create_teacher', TeacherCreateView.as_view(), name='create'),
    path('edit_teacher/<int:teacher_id>', edit_teacher, name='edit'),
    path('delete_teacher/<int:teacher_id>', delete_teacher, name='delete'),
    path('generate_teacher/', generate_teacher, name='generate'),
    path('generate_teacher/<int:qty>', generate_teachers, name='multi-generate')
]
