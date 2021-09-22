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
from .views import StudentListView

from .views import *

urlpatterns = [
    path('students/', StudentListView.as_view(), name='list-students'),
    # path('students/', list_students, name='list-students'),
    path('student/<int:student_id>', get_student, name='get-student'),
    path('create_student', create_student, name='create-student'),
    path('edit_student/<int:student_id>', edit_student, name='edit-student'),
    path('delete_student/<int:student_id>', delete_student, name='delete-student'),
    path('generate_student/', generate_student, name='generate-student'),
    path('generate_students/<int:qty>', generate_students, name='generate-students')
]
