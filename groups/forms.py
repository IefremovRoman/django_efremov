from django import forms

from .models import Group

# ["title", "start_year", "finish_year", "student_quantity"]
class GroupForm(forms.ModelForm):
    # group_choice = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Group
        fields = ['title', 'start_year', 'finish_year', 'student_quantity']
