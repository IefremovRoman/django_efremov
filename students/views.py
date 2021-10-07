from django.core.management import call_command
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, View

from django_efremov.views import PersonListView, PersonCreateView

from .forms import StudentForm
from .models import Student


# Viewers
class StudentListView(PersonListView):
    model = Student
    template_name = 'student_list.html'

    def get(self, request, student_id=None, **kwargs):
        return super(
            StudentListView,
            self).get(
            request,
            model=self.model,
            template_name=self.template_name,
            header='student',
            person_id=student_id,
            **kwargs)

    # def get(self, request, student_id=None, **kwargs):
    #     if student_id:
    #         students = Student.objects.filter(id=student_id).all()
    #     else:
    #         students = Student.objects.all()
    #
    #     students = students.order_by('id').values()
    #     paginator = Paginator(students, 18)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     return render(
    #         request,
    #         self.template_name,
    #         {
    #             'page_obj': page_obj,
    #             # 'students': students,
    #             'header': 'student',
    #             'fields': Student._meta.fields
    #         })


class StudentCreateView(CreateView):
    template_name = 'student_create_form.html'
    form_class = StudentForm

    # def create_method(self, appname='students'):
    #     return super(StudentCreateView, self).create_method(self, self.model, self.form, appname=appname)
    def form_valid(self, form):
        if Student.objects.filter(**form.cleaned_data).exists():
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
        return redirect(reverse('students:edit', kwargs={'student_id': self.get_object().id}))


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

    def get(self, request, **kwargs):
        call_command('generate_students')
        return redirect('students:list')
