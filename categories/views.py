from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def homepage(request):
    return HttpResponse("Hello")

def Category(request):
    #cat=Category.objects.all()
    #return HttpResponse(cat) 
    
    
    #return HttpResponse("Hello")
	return render(request,'YAB/Categories.html')
