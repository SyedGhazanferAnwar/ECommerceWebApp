from django.shortcuts import render
from .models import Product, Cart, Container
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def homepage(request):
    qs = Product.objects.all()
    # if request.user.is_authenticated:
    #     mcart = Cart.objects.filter(user=request.user)
    #     print(cart)

    #     if cart is not None:
    #         container = Container.objects.filter(cart=mcart[0])
    #         return HttpResponse(container)
    #         print(container)

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
        totalPrice = 0
        for i in container:
            totalPrice += i.product.price*i.quantity
        # print(container[0].product)
        return render(request, 'cart.html', {'container': container, 'cartPrice': totalPrice})


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
        cart.container.add(container)
        cart.save()
        return HttpResponse('update Cart')
    else:
        return HttpResponse('unauthenticated')
