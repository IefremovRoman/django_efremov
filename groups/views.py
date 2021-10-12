from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from students.models import Student

from teachers.models import Teacher

from .forms import GroupForm
from .models import Group


# Viewers
class GroupListView(ListView):
    model = Group
    template_name = 'group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.model._meta.fields
        context['header'] = 'group'
        return context


class GroupGetView(View):

    def get(self, request, group_id=None, **kwargs):

        if group_id:
            group = Group.objects.filter(id=group_id).all().first()
        else:
            group = Group.objects.all()

        if group is not None:
            teacher_id = group.teacher_id_id
            teacher = model_to_dict(Teacher.objects.filter(id=teacher_id).all().first())
            students = [
                model_to_dict(s) for s in Student.objects.filter(
                    group_id_id=group.id).order_by('id').all()]
            group = model_to_dict(group)
            student_fields = Student._meta.fields
            paginator = Paginator(students, 13)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        else:
            teacher, page_obj, student_fields = [], [], []

        return render(
            request,
            'group_get_view.html',
            {
                'group': group,
                'teacher': teacher,
                'page_obj': page_obj,
                'student_fields': student_fields
            }
        )

# class GroupGetView(View):
#
#     def get(self, request, group_id=1, **kwargs):
#
#         group = Group.objects.filter(id=group_id).values()[0]
#         teacher_id = group.get('teacher_id_id')
#         teacher = Teacher.objects.filter(id=teacher_id).values()[0]
#         students = [s for s in Student.objects.filter(
#             group_id=group.get('id')).order_by('id').values()]
#
#         student_fields = Student._meta.fields
#         paginator = Paginator(students, 13)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#
#         return render(
#             request,
#             'group_get_view.html',
#             {
#                 'group': group,
#                 'teacher': teacher,
#                 'page_obj': page_obj,
#                 'student_fields': student_fields
#             }
#         )

#
# class GroupGetView(View):
#
#     def get(self, request, group_id=1, **kwargs):
#
#             group = Group.objects.filter(id=group_id)
#             teacher_id = group.teacher_id_id
#             teacher = Teacher.objects.get(id=teacher_id)
#             students = [s for s in Student.objects.filter(
#                 group_id=group.id).order_by('id').values()]
#
#             student_fields = Student._meta.fields
#             paginator = Paginator(students, 13)
#             page_number = request.GET.get('page')
#             page_obj = paginator.get_page(page_number)
#
#             return render(
#                 request,
#                 'group_get_view.html',
#                 {
#                     'group': group,
#                     'teacher': teacher,
#                     'page_obj': page_obj,
#                     'student_fields': student_fields
#                 }
#             )


class GroupCreateView(CreateView):
    template_name = 'group_create_form.html'
    form_class = GroupForm

    def form_valid(self, form):
        if Group.objects.filter(**form.cleaned_data).exists():
            return redirect('groups:create')
        else:
            Group(**form.cleaned_data).save()
            return redirect('groups:list')

    def form_invalid(self, form):
        return redirect('groups:create')


class GroupUpdateView(UpdateView):
    form_class = GroupForm
    template_name = 'group_edit_form.html'
    # pk_url_kwarg = 'group_id'
    queryset = Group.objects.all()

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("group_id")
        return get_object_or_404(Group, id=id_)

    def form_valid(self, form):
        Group.objects.update_or_create(
            defaults=form.cleaned_data,
            id=self.get_object().id)
        return redirect('groups:list')

    def form_invalid(self, form):
        return redirect(reverse('groups:edit', kwargs={'group_id': self.get_object().id}))


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
