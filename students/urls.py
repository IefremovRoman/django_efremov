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

from .views import (StudentListView,
                    StudentCreateView,
                    # get_student,
                    # create_student,
                    StudentUpdateView,
                    # edit_student,
                    StudentDeleteView,
                    # delete_student,
                    StudentGenerateView,
                    # generate_student,
                    StudentMultiGenerateView
                    # generate_students
                    )

app_name = 'students'
urlpatterns = [
    path('students/',                       StudentListView.as_view(),      name='list'),
    # path('students/', list_students, name='list-students'),
    # path('student/<int:student_id>',        get_student,                    name='get'),
    path('student/<int:student_id>',        StudentListView.as_view(),      name='get'),
    # path('create_student',                  create_student,               name='create'),
    path('create_student',                  StudentCreateView.as_view(),    name='create'),
    # path('edit_student/<int:student_id>',   edit_student,                 name='edit'),
    path('edit_student/<int:student_id>',   StudentUpdateView.as_view(),    name='edit'),
    # path('delete_student/<int:student_id>', delete_student,                 name='delete'),
    path('delete_student/<int:pk>',         StudentDeleteView.as_view(),    name='delete'),
    path('generate_student/',               StudentGenerateView.as_view(),  name='generate'),
    # path('generate_student/',               generate_student,               name='generate'),
    # path('generate_students/<int:qty>',     generate_students,              name='multi-generate')
    path('generate_students/<int:qty>',     StudentMultiGenerateView.as_view(),              name='multi-generate')
]
