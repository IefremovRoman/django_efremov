from django import forms


class ContactUS(forms.Form):
    title = forms.CharField(label='Title', max_length=64)
    message = forms.CharField(label='Message', max_length=512)
    email_from = forms.EmailField(label='Send from')
