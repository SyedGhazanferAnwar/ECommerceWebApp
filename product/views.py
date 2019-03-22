from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.


def homepage(request):
<<<<<<< HEAD
    qs = Product.object.all()
    return H
=======
    qs = Product.objects.all()
    return HttpResponse(qs)
>>>>>>> b09d5d6921f5b148e68fc85e2a72c4017154df76


def product(request):
    return HttpResponse('Product')
