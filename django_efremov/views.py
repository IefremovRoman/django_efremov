from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import ContactUS
from .tasks import contact_us_send_mail


# , delayed_redirect


class PersonListView(ListView):
    # template_name = "view_list.html"
    pass


def contact_us(request):
    if request.method == 'POST':
        form = ContactUS(request.POST)
        if form.is_valid():
            contact_us_send_mail.delay(
                subject=form.cleaned_data.get('subject'),
                message=form.cleaned_data.get('message'),
                from_email=form.cleaned_data.get('email_from'),
                recipient_list=[
                    'danepe6714@sicmag.com',
                ]
            )
            # 'vitalik1996@gmail.com'
            messages.success(request, 'Your message has been sent! Thanks for you request!')
            return redirect('contact-us')
    elif request.method == 'GET':
        form = ContactUS()
        return render(request, 'contactUS.html', {'form': form})


def handler404(request, *args, **argv):
    return render(request, '404.html')


def handler500(request, *args, **argv):
    return render(request, '500.html')

# def model_pretty_viewer(query):
#     return '<br/>'.join(str(q) for q in query)


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
