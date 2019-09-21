from django import forms
# from django.forms import widgets
# from webapp.models import STATUS_CHOICES


class EntryForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Author')
    email = forms.EmailField(max_length=50, required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, label="Text")
    # status = forms.CharField(choices=STATUS_CHOICES, required=)


