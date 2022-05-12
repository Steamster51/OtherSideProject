from email import message
from django import forms

class contactForm(forms.Form):
    fullName = forms.CharField(max_length=50, label='Full Name')
    email = forms.CharField(max_length=50, label='Email', widget=forms.EmailInput)
    message = forms.CharField(widget= forms.Textarea, label="Message")