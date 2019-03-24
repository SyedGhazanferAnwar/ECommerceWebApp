from django.shortcuts import render
from Product.models import Product

def homepage(request):
    qs = Product.objects.all()
    return render(request, "index.html", {"qs": qs})