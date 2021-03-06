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
from django.urls import path

from .views import CurrencyView

urlpatterns = [
    path('currencies/', CurrencyView.as_view(), name='list-currencies'),
    # path('group/<int:group_id>', get_group, name='get-group'),
    # path('create_group', create_group, name='create-group'),
    # path('edit_group/<int:group_id>', edit_group, name='edit-group'),
    # path('delete_group/<int:group_id>', delete_group, name='delete-group')
]
