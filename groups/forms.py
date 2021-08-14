from django import forms

from .models import Group

# class Validator():
# 	def clean_first_name(self):
# 	for name in Stock.objects.filter_by():
# 				if instance.category == category:
# 					raise forms.ValidationError(str(category) + ' is already created')
# 			return category

class GroupForm(forms.ModelForm):
    # group_choice = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Group
        fields = ['student_id', 'teacher_id']

# class GroupForm(forms.Form):
#     student_id = forms.IntegerField(label="Student\'s' id")
#     teacher_id = forms.IntegerField(label="Teacher\'s' id")
