from django.shortcuts import render
from .models import Product, Cart, Container
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def homepage(request):
    qs = Product.objects.all()
    for i in qs:
        print(i.id, i.name)
    return render(request, "index.html", {"qs": qs})


def product(request, id):
    print(id)
    return render(request, 'product.html', {})


def cart(request):
    if not request.user.is_authenticated:
        return redirect('/admin')
    else: 
        mcart = get_object_or_404(Cart, user=request.user)
        container = Container.objects.filter(cart=mcart)
        for i in container:
            mcart.totalPrice += i.product.price*i.quantity
        mcart.save()
        # print(container[0].product)
        return render(request, 'cart.html', {'container': container})


# @register.simple_tag()
# def multiply(qty, unit_price, *args, **kwargs):
#     # you would need to do any localization of the result here
#     return qty * unit_price


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
        cart.totalPrice=0
        cart.container.add(container)
        cart.save()
        return HttpResponse('update Cart')
    else:
        return HttpResponse('unauthenticated')
