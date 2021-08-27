from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from faker import Faker

from .models import Student
from .forms import StudentForm

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)
    # return '<br/>'.join(map(str, query)) 

# Viewers
def list_students(request):
    student_list = [student.__dict__ for student in Student.objects.all()]
    fields = Student._meta.fields
    # output = model_pretty_viewer(student_list)
    return render(
                    request,
                    'student_list_view.html',
                    {
                        'students': student_list,
                        'fields': fields}
                        )
# class StudentListView(ListView):
#   model = Student
#   template_name  = "list_view.html"


def get_student(request, student_id):
    if student_id:
        student = Student.objects.filter(id=student_id)
        # fields = Student._meta.fields
        output = model_pretty_viewer(student)
        return HttpResponse(output)

    return redirect('list-students')


def create_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if Student.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                messages.error(request, 'This data is doubling!')
                return redirect('create-student')
                
            else:
                Student(**form.cleaned_data).save()
                return redirect('list-students')
        
        else:
            messages.error(request, 'Invalid phone format! Please, try again.')
            return redirect('create-student')

    elif request.method == 'GET':
        form = StudentForm()
    return render(
                    request,
                    'student_create_form.html',
                    {
                        'form': form,
                    })


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # if Student.objects.filter(**form.cleaned_data).exists():
            #    messages.error(request, 'This data is doubling!')
                # return redirect('edit-student')
            # else:    
            Student.objects.update_or_create(
                                            defaults=form.cleaned_data,
                                            id=student_id)
            return redirect('list-students')
        
        else:
            messages.error(request, 'Invalid phone format! Please, try again.')
            return redirect('edit-students')

    elif request.method == 'GET':
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(instance=student)

        return render(
                        request,
                        'student_edit_form.html',
                        {
                            'form': form,
                            'student_id': student_id
                        })
    
    else:
        return HttpResponse('Method not registered')


def delete_student(request, student_id):
    student = Student.objects.filter(id=student_id)
    student.delete()
    return redirect('list-students')


def generate_student(request):

    Student.objects.create(
                            first_name=faker.first_name(),
                            last_name=faker.last_name(),
                            age=faker.random_int(min=17, max=30),
                            phone=f'+38000{faker.msisdn()[0:7]}'
                            )
    
    return redirect('list-students')


def generate_students(request, qty=100):
    # if request.method == 'GET':

        # count = request.GET.get('count', '100')
        # try:
        #     count = int(count)
        # except ValueError:
        #     return HttpResponse(f'{count} not integer')

        # if count <= 100 and count > 0:

    for i in range(int(qty)):
        Student.objects.create(
                        first_name=faker.first_name(),
                        last_name=faker.last_name(),
                        age=faker.random_int(min=17, max=30),
                        phone=f'+38000{faker.msisdn()[0:7]}'
                        )
    
    return redirect('list-students')
    # return HttpResponse('Method not found')


# def create_student(request, student_id):
#   if request.method = 'POST':
#     form = StudentFormFromModel(request.POST)
#     if form.is_valid():
#      Student.object.update_or_create(defaults=form.cleaned_data, id=student_id)
#      return HttpResponseRedirect(reverse('list_students'))
