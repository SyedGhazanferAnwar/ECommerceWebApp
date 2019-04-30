from django.shortcuts import render, redirect
from newsletter.views import newsletter_signup_home

# Create your views here.
def our_story(request):
    form = newsletter_signup_home(request)
    return render(request, "aboutus.html",{"form":form})

def our_story_redirect(request):
    return redirect('/about/our-story')