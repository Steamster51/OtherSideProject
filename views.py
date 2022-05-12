from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contactForm
from .models import contactmsg

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        contactFormData = contactForm(request.POST)
        if contactFormData.is_valid():
            fullName = contactFormData.cleaned_data['fullName']
            email = contactFormData.cleaned_data['email']
            message = contactFormData.cleaned_data['message']
            insertdata = contactmsg(dbfullName = fullName, dbemail = email, dbmessage = message)
            insertdata.save()
            form = contactForm()
            msgtouser = "We will get back to you!"
            return render(request, 'pages/contact.html', {'Form' : form, 'feedback' : msgtouser})
    else:
        error = "Send us an email, or if you did, something went wrong!"
        form = contactForm()
        return render(request, 'pages/contact.html', {'Form' : form, 'Error' : error})

def map(request):
    return render(request, 'pages/map.html')

def services(request):
    return render(request, 'pages/services.html')
