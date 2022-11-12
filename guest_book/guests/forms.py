from django import forms

class GuestForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    email_address = forms.CharField(label='Email')
    message = forms.CharField(widget=forms.Textarea)