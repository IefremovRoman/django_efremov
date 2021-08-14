from django import forms

from .models import Group, Student, Teacher

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
        fields = ['first_name', 'last_name', 'age']

class GroupForm(forms.ModelForm):
    # group_choice = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Group
        fields = ['student_id', 'teacher_id']

class TeacherForm(forms.ModelForm):
    # teacher_choice = forms.ModelChoiceField(queryset=Teacher.objects.all())
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'subject']

# class StudentForm(forms.Form):
    # first_name = forms.CharField(label="Student\'s' first name", max_length=24)
    # last_name = forms.CharField(label="Student\'s' last name", max_length=24)
    # age = forms.IntegerField(label="Student\'s' age",)


# class GroupForm(forms.Form):
#     student_id = forms.IntegerField(label="Student\'s' id")
#     teacher_id = forms.IntegerField(label="Teacher\'s' id")


# class TeacherForm(forms.Form):
#     first_name = forms.CharField(label="Teacher\'s' first name", max_length=24)
#     last_name = forms.CharField(label="Teacher\'s' last name", max_length=24)
#     age = forms.IntegerField(label="Teacher\'s' age")
#     subject = forms.CharField(label="Teacher\'s' subject", max_length=24)


