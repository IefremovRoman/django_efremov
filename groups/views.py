from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from faker import Faker

from .models import Group
# from .forms import GroupForm

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


def model_pretty_viewer(query):
	return '<br/>'.join(str(q) for q in query)
	# return '<br/>'.join(map(str, query)) 

# Viewers
def groups(request):
    group_list = Group.objects.all()
    output = model_pretty_viewer(group_list)
    return HttpResponse(output)


def create_group(request):

    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            if Group.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                operation_status = {
                    'text': 'This data is doubling!',
                    'app_link_text': 'Group',
                    'app_list': 'groups/'
                    }
                return render(request, 'operation_status.html', operation_status)
                
            else:
                Group.objects.create(**form.cleaned_data)
                operation_status = {
                    'text': 'Group created successfully!',
                    'app_link_text': 'Group',
                    'app_list': 'groups/'
                    }
                return render(request, 'operation_status.html', operation_status)

    elif request.method == 'GET':
        form = GroupForm()
    return render(
                    request,
                    'creation_form.html',
                    {
                        'form': form,
                        'header':'Group creation form',
                        'action':'/create_group',
                        'app_link_text': 'Group',
                        'app_list': 'groups/'
                    })

