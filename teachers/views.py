from django.contrib.messages.views import SuccessMessageMixin
from django.core.management import call_command
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, View

from django_efremov.views import PersonListView

from .forms import TeacherForm
from .models import Teacher


# Viewers
class TeacherListView(PersonListView, View):
    model = Teacher
    template_name = 'teacher_list.html'

    # paginate_by = 18  # OR WHATEVER NUMBER YOU DESIRE PER PAGE
    # pagination_class = Paginator  # OR NumberDetailPagination

    def get(self, request, teacher_id=None, **kwargs):
        if teacher_id:
            teachers = Teacher.objects.filter(id=teacher_id).all()
        else:

            teachers = Teacher.objects.all()
        teachers = teachers.values()
        paginator = Paginator(teachers, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            self.template_name,
            {
                'page_obj': page_obj,
                # 'teachers': teachers,
                'header': 'teacher',
                'fields': Teacher._meta.fields
            })


class TeacherCreateView(CreateView, SuccessMessageMixin):
    template_name = 'teacher_create_form.html'
    form_class = TeacherForm

    def form_valid(self, form):
        if Teacher.objects.filter(**form.cleaned_data).exists():
            return redirect('teachers:create')
        else:
            Teacher(**form.cleaned_data).save()
            return redirect('teachers:list')

    def form_invalid(self, form):
        return redirect('teachers:create')


class TeacherUpdateView(UpdateView):
    form_class = TeacherForm
    template_name = 'teacher_edit_form.html'
    # pk_url_kwarg = 'teacher_id'
    queryset = Teacher.objects.all()

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("teacher_id")
        return get_object_or_404(Teacher, id=id_)

    def form_valid(self, form):
        Teacher.objects.update_or_create(
            defaults=form.cleaned_data,
            id=self.get_object().id)
        return redirect('teachers:list')

    def form_invalid(self, form):
        return redirect('teachers:edit')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')

    # template_name = 'teacher_confirm_delete.html'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class TeacherGenerateView(View):
    # url = None
    # pattern_name = 'teachers:list'

    def get(self, *args, **kwargs):
        call_command('generate_teachers', total=1)
        return redirect('teachers:list')


class TeacherMultiGenerateView(View):

    def get(self, request, **kwargs):
        call_command('generate_teachers')
        return redirect('teachers:list')

# def teachers(request):
#     if request.method == 'GET':
#
#         query = Teacher.objects.all()
#         first_name = request.GET.get('first_name', '')
#         if first_name:
#             query = query.filter(first_name=first_name)
#
#         last_name = request.GET.get('last_name', '')
#         if last_name:
#             query = query.filter(last_name=last_name)
#
#         age = request.GET.get('age', '')
#         if age:
#             query = query.filter(age=age)
#
#         subject = request.GET.get('subject', '')
#         if subject:
#             query = query.filter(subject=subject)
#
#         output = model_pretty_viewer(query)
#         return HttpResponse(output)
#     return HttpResponse('Method not found')
