from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message
from django.http import HttpResponseRedirect
from django.contrib import messages
from Product.models import Category
from Product.views import get_product_count
# Create your views here.

def contactForm(request):
    if request.method == 'GET':
        form = ContactForm()
    else: 
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg_instance = Message.objects.create(firstName = first_name, lastName = last_name, email = email, subject = subject ,message = message)
            messages.success(request,'Form submission successful')
            return HttpResponseRedirect('')
    return render(request, 'contact.html',{'form':form,"qsc":Category.objects.all(),"product_count": get_product_count(request)})