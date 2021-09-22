import json
from random import choice
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.views.generic import ListView
from django.contrib import messages

from faker import Faker

from .models import Teacher
from .forms import TeacherForm

from django_efremov.views import PersonListView

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)
subject_json = 'teachers/management/commands/university_subjects.json'


def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)
    # return '<br/>'.join(map(str, query)) 

# Viewers
def teachers(request):
    if request.method == 'GET':

        query = Teacher.objects.all()
        first_name = request.GET.get('first_name', '')
        if first_name:
            query = query.filter(first_name=first_name)

        last_name = request.GET.get('last_name', '')
        if last_name:
            query = query.filter(last_name=last_name)

        age = request.GET.get('age', '')
        if age:
            query = query.filter(age=age)

        subject = request.GET.get('subject', '')
        if subject:
            query = query.filter(subject=subject)

        output = model_pretty_viewer(query)
        return HttpResponse(output)
    return HttpResponse('Method not found')


# Viewers
class TeacherListView(PersonListView):
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'teacher'
        context['fields'] = Teacher._meta.fields
        return context

# def list_teachers(request):
#     teacher_list = [teacher.__dict__ for teacher in Teacher.objects.all()]
#     fields = Teacher._meta.fields
#     # output = model_pretty_viewer(teacher_list)
#     return render(
#                     request,
#                     'teacher_list_view.html',
#                     {
#                         'teachers': teacher_list,
#                         'fields': fields
#                     }
#                 )


def get_teacher(request, teacher_id):
    if teacher_id:
        teacher = Teacher.objects.filter(id=teacher_id)
        # fields = teacher._meta.fields
        output = model_pretty_viewer(teacher)
        return HttpResponse(output)

    return redirect('list-teachers')


def create_teacher(request):
    
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            if Teacher.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                messages.error(request, 'This data is doubling!')
                return redirect('create-teacher')
                
            else:
                Teacher(**form.cleaned_data).save()
                return redirect('list-teachers')

        else:
            messages.error(request, 'Invalid phone format! Please, try again.')
            return redirect('create-teacher')

    elif request.method == 'GET':
        form = TeacherForm()
    return render(
                    request,
                    'teacher_create_form.html',
                    {
                        'form': form,
                    })


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            # if teacher.objects.filter(**form.cleaned_data).exists():
            #    messages.error(request, 'This data is doubling!')
                # return redirect('edit-teacher')
            # else:    
            Teacher.objects.update_or_create(
                                            defaults=form.cleaned_data,
                                            id=teacher_id)
            return redirect('list-teachers')

        else:
            messages.error(request, 'Invalid phone format! Please, try again.')
            return redirect('edit-teacher')

    elif request.method == 'GET':
        teacher = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherForm(instance=teacher)

        return render(
                        request,
                        'teacher_edit_form.html',
                        {
                            'form': form,
                            'teacher_id': teacher_id,
                        })

    else:
        return HttpResponse('Method not registered')


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.filter(id=teacher_id)
    teacher.delete()
    return redirect('list-teachers')


def generate_teacher(request):
    with open(subject_json, 'r') as file:
            subjects = json.load(file)

    Teacher.objects.create(
                            first_name=faker.first_name(),
                            last_name=faker.last_name(),
                            age=faker.random_int(min=26, max=100),
                            subject=choice(subjects),
                            phone=f'+38000{faker.msisdn()[0:7]}'
                            )
    
    return redirect('list-teachers')


def generate_teachers(request, qty=100):
    # if request.method == 'GET':

        # count = request.GET.get('count', '100')
        # try:
        #     count = int(count)
        # except ValueError:
        #     return HttpResponse(f'{count} not integer')

        # if count <= 100 and count > 0:

    with open(subject_json, 'r') as file:
            subjects = json.load(file)

    for _ in range(int(qty)):
        Teacher.objects.create(
                        first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        age=faker.random_int(min=26, max=100),
                        subject=choice(subjects),
                        phone=f'+38000{faker.msisdn()[0:7]}'
                        )
    
    return redirect('list-teachers')
    # return HttpResponse('Method not found')


# def create_teacher(request, teacher_id):
#   if request.method = 'POST':
#     form = teacherFormFromModel(request.POST)
#     if form.is_valid():
#      teacher.object.update_or_create(defaults=form.cleaned_data, id=teacher_id)
#      return HttpResponseRedirect(reverse('list_teachers'))



# def create_teacher(request, teacher_id):
#    if request.method = 'POST':
#       form = teacherFormFromModel(request.POST)
#       if form.is_valid():
#          teacher.object.update_or_create(defaults=form.cleaned_data, id=teacher_id)
#          return HttpResponseRedirect(reverse('list_teachers'))
