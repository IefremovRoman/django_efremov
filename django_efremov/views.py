from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')

def model_pretty_viewer(query):
    return '<br/>'.join(str(q) for q in query)


# from django.urls import path
# def list_view_factory(model, entity):
# 	def list_view(request):
# 	    object_list = model.objects.all()
# 	    output = model_pretty_viewer(object_list)
# 	    return HttpResponse(output)

# 	urlpatterns = [
#     # path('students/', StudentListView.as_view()),
# 	    path(f'{entity}/', list_view),
# 	    ...
# 	]


# 	return urlpatterns

# path('', include(list_view_factory(Student, 'students'))),


# class StudentListView(ListView):
#     model = Student
#     template_name = "list_view.html"


# def create_factory(FormClass, model):
# 	def create(request):
	    
# 	    if request.method == 'POST':
# 	        form = FormClass(request.POST)
# 	        if form.is_valid():
# 	            if model.objects.filter(**form.cleaned_data).exists():
# 	                # raise forms.ValidationError('This data is doubling!')
# 	                operation_status = {
# 	                    'text': 'This data is doubling!',
# 	                    'app_link_text': 'Student',
# 	                    'app_list': 'students/'
# 	                    }
# 	                return render(request, 'operation_status.html', operation_status)
	                
# 	            else:
# 	                Student.objects.create(**form.cleaned_data)
# 	                operation_status = {
# 	                    'text': 'Student created successfully!',
# 	                    'app_link_text': 'Student',
# 	                    'app_list': 'students/'
# 	                    }
# 	                return render(request, 'operation_status.html', operation_status)

# 	    elif request.method == 'GET':
# 	        form = StudentForm()
# 	    return render(
# 	                    request,
# 	                    'creation_form.html',
# 	                    {
# 	                        'form': form,
# 	                        'header':'Student creation form',
# 	                        'action':'/create_student',
# 	                        'app_link_text': 'Student',
# 	                        'app_list': 'students/'
# 	                    })