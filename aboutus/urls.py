from django.contrib import admin
from django.urls import path
from .views import our_story, our_story_redirect

#make urls here
urlpatterns = [
    path('',our_story_redirect),
    path('our-story',our_story, name='aboutus'),
    path('our-story/',our_story_redirect)
]
    