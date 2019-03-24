from django.shortcuts import render
from .models import Cart, Container
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def product(request, id):
    print(id)
    return render(request, 'product.html', {})


def cart(request):
    return render(request, 'cart.html', {})

def addtocart(request, id, quantity):
    print(request.user)
    print("Asdasdsad", quantity)
    if request.user.is_authenticated:
        print("n000000")
        print(id)
        product = get_object_or_404(Product, pk=id)
        i_user = request.user
        cart, created = Cart.objects.get_or_create(user=i_user)
        container, created = Container.objects.get_or_create(
            product=product)
        container.product = product
        container.quantity = quantity
        container.save()
        cart.user = i_user
        cart.container.add(container)
        cart.save()
        return HttpResponse('update Cart')
    else:
        return HttpResponse('unauthenticated')
