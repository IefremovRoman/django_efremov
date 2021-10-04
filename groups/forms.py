from django import forms

from .models import Group


class GroupForm(forms.ModelForm):
    # group_choice = forms.ModelChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Group
        fields = ['title', 'start_year', 'finish_year', 'student_quantity', 'teacher_id']

    # def clean_start_year(self):
    # 	start_year = self.cleaned_data['start_year']
    # 	if 1984 < start_year < 2021:
    # 		raise forms.ValidationError('Not valid start year. Put smth btwn 1984 and 2021')
    # 	return start_year