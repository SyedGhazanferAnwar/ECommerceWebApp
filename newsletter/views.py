from django.shortcuts import render
from .models import NewsUser
from .forms import NewsUserForm

# Create your views here.
def newsletter_signup_home(request):
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            #check if email already exists
            newEmail = form.cleaned_data['email']
            if NewsUser.objects.filter(email = newEmail).exists():
                print('Email already subscribed')
                form = NewsUserForm()
            else:
                NewsUser.objects.create(email = newEmail)
                form = NewsUserForm()
    else:
        form = NewsUserForm()
    return form