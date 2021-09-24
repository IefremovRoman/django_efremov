from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.management import call_command
from django.views.generic import View, ListView, FormView, CreateView, UpdateView, DeleteView

from faker import Faker

from .models import Student
from .forms import StudentForm

from django_efremov.views import PersonListView

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)
    # return '<br/>'.join(map(str, query))


# Viewers
class StudentListView(PersonListView, View):
    model = Student
    template_name = 'student_list.html'

    # paginate_by = 10  # OR WHATEVER NUMBER YOU DESIRE PER PAGE
    # pagination_class = Paginator  # OR NumberDetailPagination

    def get(self, request, student_id=None, **kwargs):
        if student_id:
            students = Student.objects.filter(id=student_id).all()
        else:
            students = Student.objects.all()
        return render(
            request,
            self.template_name,
            {
                'students': students,
                'header': 'student',
                'fields': Student._meta.fields
            })

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['header'] = 'student'
    #     context['fields'] = Student._meta.fields
    #     return context


# def list_students(request):
#     students = [student.__dict__ for student in Student.objects.all()]
#     fields = Student._meta.fields
#     return render(
#         request,
#         'student_list_view.html',
#         {
#             'students': students,
#             'fields': fields
#         }
#     )

####
# def get_student(request, student_id):
#     if student_id:
#         student = Student.objects.filter(id=student_id)
#         # fields = Student._meta.fields
#         output = model_pretty_viewer(student)
#         return HttpResponse(output)
#
#     return redirect('list-students')
####

# def create_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             if Student.objects.filter(**form.cleaned_data).exists():
#                 # raise forms.ValidationError('This data is doubling!')
#                 messages.error(request, 'This data is doubling!')
#                 return redirect('create-student')
#
#             else:
#                 Student(**form.cleaned_data).save()
#                 return redirect('list-students')
#
#         else:
#             messages.error(request, 'Invalid phone format! Please, try again.')
#             return redirect('create-student')
#
#     elif request.method == 'GET':
#         form = StudentForm()
#     return render(
#         request,
#         'student_create_form.html',
#         {
#             'form': form,
#         })
class StudentCreateView(CreateView, SuccessMessageMixin):
    template_name = 'student_create_form.html'
    form_class = StudentForm

    def form_valid(self, form):
        if Student.objects.filter(**form.cleaned_data).exists():
            # raise forms.ValidationError('This data is doubling!')
            #     messages.error(request, 'This data is doubling!')
            #     self.get_context_data(('success_message', 123))
            #     context = self.get_context_data()
            #     context.update({'success_message': 123})
            return redirect('students:create')
        else:
            Student(**form.cleaned_data).save()
            return redirect('students:list')

    def form_invalid(self, form):
        return redirect('students:create')


class StudentUpdateView(UpdateView):
    form_class = StudentForm
    template_name = 'student_edit_form.html'
    # pk_url_kwarg = 'student_id'
    queryset = Student.objects.all()

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("student_id")
        return get_object_or_404(Student, id=id_)

    def form_valid(self, form):
        Student.objects.update_or_create(
            defaults=form.cleaned_data,
            id=self.get_object().id)
        return redirect('students:list')

    def form_invalid(self, form):
        return redirect('students:edit')


# def edit_student(request, student_id):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             Student.objects.update_or_create(
#                                             defaults=form.cleaned_data,
#                                             id=student_id)
#             return redirect('list-students')
#
#         else:
#             messages.error(request, 'Invalid phone format! Please, try again.')
#             return redirect('edit-students')
#
#     elif request.method == 'GET':
#         student = Student.objects.filter(id=student_id).first()
#         form = StudentForm(instance=student)
#
#         return render(
#             request,
#             'student_edit_form.html',
#             {
#                 'form': form,
#                 'student_id': student_id
#             })
#
#     else:
#         return HttpResponse('Method not registered')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    # template_name = 'student_confirm_delete.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class StudentGenerateView(View):
    # url = None
    # pattern_name = 'students:list'

    def get(self, *args, **kwargs):
        call_command('generate_students', total=1)
        return redirect('students:list')


class StudentMultiGenerateView(View):

    def get(self, request, qty=100, **kwargs):
        call_command('generate_students')
        return redirect('students:list')
