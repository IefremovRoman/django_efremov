from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

from faker import Faker

from .models import Group
from teachers.models import Teacher
from students.models import Student
from .forms import GroupForm

# Help funcitons
locale = 'uk_UA'
faker = Faker(locale)


def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)
    # return '<br/>'.join(map(str, query)) 

# Viewers
def list_groups(request):
    group_list = [group.__dict__ for group in Group.objects.all()]
    teachers_id = [g.get('teacher_id_id') for g in group_list]
    teachers = [Teacher.objects.filter(id=t_id).values()[0] for t_id in teachers_id]
    groups = [{'teacher': teacher, 'group': group} for teacher, group in zip(teachers, group_list)]
    student_queryset = [Student.objects.filter(group_id=g.get('id')).values() for g in group_list]
    # students = [student for subset in student_queryset for student in subset]
    students = []
    breakpoint()
    return render(
                    request,
                    'group_list_view.html',
                    {
                        'groups': groups,
                        'students': students
                    }
                )
# def list_groups(request):
#     group = Group.objects.all()
#     output = model_pretty_viewer(group)
#     return HttpResponse(output)

def get_group(request, group_id):
    if group_id:
        group = Group.objects.filter(id=group_id)
        # fields = group._meta.fields
        output = model_pretty_viewer(group)
        return HttpResponse(output)

    return redirect('list-groups')


def create_group(request):
    
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            if Group.objects.filter(**form.cleaned_data).exists():
                # raise forms.ValidationError('This data is doubling!')
                messages.error(request, 'This data is doubling!')
                return redirect('create-group')
                
            else:
                Group(**form.cleaned_data).save()
                return redirect('list-groups')
        
        else:
            messages.error(request, 'Start or finish year is exceeded limits! Please, try again.')
            return redirect('create-group')

    elif request.method == 'GET':
        form = GroupForm()
    return render(
                    request,
                    'group_create_form.html',
                    {
                        'form': form,
                    })


def edit_group(request, group_id):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            # if group.objects.filter(**form.cleaned_data).exists():
            #    messages.error(request, 'This data is doubling!')
                # return redirect('edit-group')
            # else:    
            Group.objects.update_or_create(
                                            defaults=form.cleaned_data,
                                            id=group_id)
            return redirect('list-groups')
        
        else:
            messages.error(request, 'Start or finish year is exceeded limits! Please, try again.')
            return redirect('edit-group', group_id)
    
    elif request.method == 'GET':
        group = Group.objects.filter(id=group_id).first()
        form = GroupForm(instance=group)

        return render(
                        request,
                        'group_edit_form.html',
                        {
                            'form': form,
                            'group_id': group_id
                        })
    
    else:
        return HttpResponse('Method not registered')


def delete_group(request, group_id):
    group = Group.objects.filter(id=group_id)
    group.delete()
    return redirect('list-groups')
