from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    qs = Product.objects.all()
    return HttpResponse(qs)


def product(request):
    return HttpResponse('Product')
