from django import forms

from .models import Student

# class Validator():
# 	def clean_first_name(self):
# 	for name in Stock.objects.filter_by():
# 				if instance.category == category:
# 					raise forms.ValidationError(str(category) + ' is already created')
# 			return category

class StudentForm(forms.ModelForm):
    # student_choice = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone', 'group_id']

# class StudentForm(forms.Form):
    # first_name = forms.CharField(label="Student\'s' first name", max_length=24)
    # last_name = forms.CharField(label="Student\'s' last name", max_length=24)
    # age = forms.IntegerField(label="Student\'s' age",)
