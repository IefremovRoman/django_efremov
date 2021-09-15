from django import forms


class ContactUS(forms.Form):
    subject = forms.CharField(label='subject', max_length=64)
    message = forms.CharField(label='Message', max_length=512)
    email_from = forms.EmailField(label='Send from')
