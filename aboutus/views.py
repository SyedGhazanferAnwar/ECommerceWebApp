from django.shortcuts import render
from newsletter.views import newsletter_signup_home

# Create your views here.
def about_us(request):
    form = newsletter_signup_home(request)
    return render(request, 'aboutus.html',{"form":form})