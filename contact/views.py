from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def contactForm(request):
    if request.method == 'GET':
        form = ContactForm()
    else: 
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(first_name); print(last_name); print(subject); print(message)
            return HttpResponse('{"status":"Success"}');
    return render(request, 'contact.html',{'form':form})