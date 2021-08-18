from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.views.generic import ListView
from django.contrib import messages

from faker import Faker

from .models import Student
from .forms import StudentForm

# from django_efremov.views import list_view_factory

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)
    # return '<br/>'.join(map(str, query)) 

# students = list_view_factory(Student)

# Viewers
def students(request):
    student_list = Student.objects.all()
    output = model_pretty_viewer(student_list)
    return HttpResponse(output)
# class StudentListView(ListView):
#     model = Student
#     template_name  = "list_view.html"


def create_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if Student.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                # operation_status = {
                #     'text': 'This data is doubling!',
                #     'app_link_text': 'Student',
                #     'app_list': 'students/'
                #     }
                messages.error(request, 'This data is doubling!')
                # return render(request, 'operation_status.html', operation_status)
                return redirect('create-student')
                
            else:
                Student.objects.create(**form.cleaned_data)
                operation_status = {
                    'text': 'Student created successfully!',
                    'app_link_text': 'Student',
                    'app_list': 'students/'
                    }
                return render(request, 'operation_status.html', operation_status)

    elif request.method == 'GET':
        form = StudentForm()
    return render(
                    request,
                    'creation_form.html',
                    {
                        'form': form,
                        'header':'Student creation form',
                        'action':'/create_student',
                        'app_link_text': 'Student',
                        'app_list': 'students/'
                    })



def generate_student(request):

    Student.objects.create(
                            first_name=faker.first_name(),
                            last_name=faker.last_name(),
                            age=faker.random_int(min=17, max=30)
                            )
    student_list = Student.objects.all()
    output = model_pretty_viewer(student_list)
    return HttpResponse(output)


def generate_students(request):
    if request.method == 'GET':

        count = request.GET.get('count', '100')
        try:
            count = int(count)
        except ValueError:
            return HttpResponse(f'{count} not integer')

        if count <= 100 and count > 0:

            for i in range(int(count)):
                Student.objects.create(
                                first_name=faker.first_name(),
                                last_name=faker.last_name(),
                                age=faker.random_int(min=17, max=30)
                                )
        student_list = Student.objects.all()
        output = model_pretty_viewer(student_list)
        return HttpResponse(output)
    return HttpResponse('Method not found')


# def create_student(request, student_id):
#    if request.method = 'POST':
#       form = StudentFormFromModel(request.POST)
#       if form.is_valid():
#          Student.object.update_or_create(defaults=form.cleaned_data, id=student_id)
#          return HttpResponseRedirect(reverse('list_students'))
