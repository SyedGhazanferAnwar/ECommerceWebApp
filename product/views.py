from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return HttpResponse('Hello world')


def product(request):
    return HttpResponse('Product')
