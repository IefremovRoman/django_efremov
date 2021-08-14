from django import forms

from .models import Teacher

# class Validator():
# 	def clean_first_name(self):
# 	for name in Stock.objects.filter_by():
# 				if instance.category == category:
# 					raise forms.ValidationError(str(category) + ' is already created')
# 			return category

class TeacherForm(forms.ModelForm):
    # teacher_choice = forms.ModelChoiceField(queryset=Teacher.objects.all())
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'subject']

# class TeacherForm(forms.Form):
#     first_name = forms.CharField(label="Teacher\'s' first name", max_length=24)
#     last_name = forms.CharField(label="Teacher\'s' last name", max_length=24)
#     age = forms.IntegerField(label="Teacher\'s' age")
#     subject = forms.CharField(label="Teacher\'s' subject", max_length=24)
