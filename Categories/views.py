from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def category(request):
    return HttpResponse('This page will show up categories.')

#~/AHussam/