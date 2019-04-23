from django.shortcuts import render
from .models import Product, Cart, Container, Category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def get_product_count(request):
    if request.user.is_authenticated:
        mcart = Cart.objects.filter(user=request.user)
        if cart is not None:
            container = Container.objects.filter(cart=mcart[0])
            return len(container)
        return 0
    else:
        return 0


def category(request, cat):
    qs = Product.objects.filter(category__name=cat)
    qsc = Category.objects.all()
    print(qsc)
    return render(request, "categories.html", {"qs": qs, "product_count": get_product_count(request), "qsc": qsc})


def homepage(request):
    qs = Product.objects.all()

    return render(request, "index.html", {"qs": qs, "product_count": get_product_count(request)})


def product(request, id):
    print('I am heeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrew')
    ProductObj = get_object_or_404(Product, pk=id)
    return render(request, 'product.html', {'product': ProductObj})


def cart(request):
    if not request.user.is_authenticated:
        return redirect('/admin')
    else:
        mcart = Cart.objects.filter(user=request.user)
        if len(mcart) <= 0:
            return render(request, 'cart.html', {'container': None, 'cartPrice': None})
        else:
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

def clearCart(request):
    mcart = get_object_or_404(Cart, user=request.user)
    Container.objects.filter(cart=mcart).delete()
    Cart.objects.filter(user=request.user).delete()
    print("clearCart")
    return HttpResponse("Sucessfully Cleared")


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
