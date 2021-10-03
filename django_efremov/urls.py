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

# from django.core.exceptions import
# from django.http import HttpResponse
# from django.test import SimpleTestCase, override_settings

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contact_us', contact_us, name='contact-us'),
    path('', include('groups.urls')),
    path('', include('service_apps.urls')),
    path('', include('students.urls', namespace='students')),
    path('', include('teachers.urls', namespace='teachers'))
]

handler404 = 'django_efremov.views.handler404'
handler500 = 'django_efremov.views.handler500'

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns

    urlpatterns.append(path(
        r'tests_error500/',
        TemplateView.as_view(template_name='500.html'),
        name='test500')
    )

    urlpatterns.append(path(
        r'tests_error404/',
        TemplateView.as_view(template_name='404.html'),
        name='test404')
    )
