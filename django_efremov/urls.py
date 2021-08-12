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
from django.contrib import admin
from django.urls import path

from students.views import *

# from students.views import (create_student,
#                             create_group
#                             generate_student,
#                             generate_students,
#                             groups,
#                             index,
#                             students,
#                             teachers)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', students),
    path('groups/', groups),
    path('teachers/', teachers),
    path('create_student', create_student),
    path('create_group', create_group),
    path('create_teacher', create_teacher),
    path('generate-student/', generate_student),
    path('generate-students/', generate_students)
]