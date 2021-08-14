from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from faker import Faker

from .models import Teacher
from .forms import TeacherForm

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


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

def create_teacher(request):
    
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            if Teacher.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                operation_status = {
                    'text': 'This data is doubling!',
                    'app_link_text': 'Teacher',
                    'app_list': 'teachers/'
                    }
                return render(request, 'operation_status.html', operation_status)
                
            else:
                Teacher.objects.create(**form.cleaned_data)
                operation_status = {
                    'text': 'Teacher created successfully!',
                    'app_link_text': 'Teacher',
                    'app_list': 'teachers/'
                    }
                return render(request, 'operation_status.html', operation_status)

    elif request.method == 'GET':
        form = TeacherForm()
    return render(
                    request,
                    'creation_form.html',
                    {
                        'form': form,
                        'header':'Teacher creation form',
                        'action':'/create_teacher',
                        'app_link_text': 'Teacher',
                        'app_list': 'teachers/'
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






