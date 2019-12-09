from django.shortcuts import render
from .models import Product, Cart, Container, Category,singleImage,UID
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from newsletter.views import newsletter_signup_home
from django.db.models import Q
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from user.models import User
# Create your views here.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def get_product_count(request):
    try:
        if request.user.is_authenticated:
            mcart = Cart.objects.filter(user=request.user)
            if cart is not None:
                container = Container.objects.filter(cart=mcart[0])
                return len(container)
            return 0
        else:
            return 0
        return 0
    except:
        return 0


def category(request, cat):
    qs = Product.objects.filter(category__name=cat)
    count = len(qs)
    qsc = Category.objects.all()
    form = newsletter_signup_home(request)
    des = get_object_or_404(Category, name=cat)
    print(qsc)
    return render(request, "categories.html", {
        "qs": qs,
        "product_count": get_product_count(request),
        "qsc": qsc,
        "catName": cat,
        "des": des.description,
        "form": form,
        "count": count
    })


def homepage(request):
    print(request.COOKIES)
    qs = Product.objects.all()
    qsc = Category.objects.all()
    form = newsletter_signup_home(request)

    return render(request, "index.html", {"form": form, "qs": qs, "product_count": get_product_count(request), "qsc": qsc})


def product(request, id):
    qsc = Category.objects.all()
    print('I am heeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrew')
    ProductObj = get_object_or_404(Product, pk=id)
    related_prods = Product.objects.filter(
        category=ProductObj.category).exclude(pk=id)[:4]
    zimages=singleImage.objects.filter(product=ProductObj)
    print(related_prods)
    print(zimages)
    return render(request, 'product.html', {"qsc": qsc, 'product': ProductObj, 'related': related_prods, "product_count": get_product_count(request),"zimages":zimages})


@login_required(login_url='/login')
def cart(request):
    qsc = Category.objects.all()
    if not request.user.is_authenticated:
        return redirect('/admin')
    else:
        mcart = Cart.objects.filter(user=request.user)
        if len(mcart) <= 0:
            return render(request, 'cart.html', {'container': None, 'cartPrice': None, "qsc": qsc, "product_count": get_product_count(request)})
        else:
            container = Container.objects.filter(cart=mcart[0])
            totalPrice = 0
            for i in container:
                totalPrice += i.product.price*i.quantity
            # print(container[0].product)
            return render(request, 'cart.html', {"qsc": qsc, 'container': container, 'cartPrice': totalPrice, "product_count": get_product_count(request)})


# @register.simple_tag()
# def multiply(qty, unit_price, *args, **kwargs):
#     # you would need to do any localization of the result here
#     return qty * unit_price

def updateCart(request):
    if request.method == 'POST':
        print("YALLAH HABIBI")
        item_ids = request.POST.get('item_ids')
        quantity = request.POST.get('quantity')
        # print(item_ids[1])
        # print(quantity[1])
        item_ids=item_ids.split(",")
        quantity=quantity.split(",")
        for i in range(0, len(item_ids)):
            cart = Cart.objects.get(user=request.user)
            yproduct = Product.objects.get(pk=item_ids[i])
            container = Container.objects.get(product=yproduct, cart=cart)
            container.quantity = quantity[i]
            container.save()
    return HttpResponse("UPDATED")


def clearCart(request):
    mcart = get_object_or_404(Cart, user=request.user)
    Container.objects.filter(cart=mcart).delete()
    Cart.objects.filter(user=request.user).delete()
    print("clearCart")
    return HttpResponse("Sucessfully Cleared")

import time
def sleep():
    time.sleep(5)
    return


def removeItemFromCart(request):
    if request.method == "POST":
        item_id = request.POST.get("item_id")    
        mcart=get_object_or_404(Cart, user=request.user)
        pproduct=get_object_or_404(Product, pk=item_id)
        Container.objects.filter(cart=mcart).filter(product=pproduct).delete()
        return HttpResponse('Sucessfully Deleted')
    else:
        return HttpResponse('NOTHING')
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
            product=product, cart=cart)
        container.product = product
        container.quantity = quantity
        container.save()
        cart.user = i_user
        cart.container.add(container)
        cart.save()
        return HttpResponse('update Cart')
    else:
        return HttpResponse("unauthenticated")


def query(request):
    query = request.GET['search']
    print(query)
    qset = Q()
    for term in query.split():
        qset |= Q(name__contains=term)
    products = Product.objects.filter(qset)
    print(products)
    return render(request, "search.html", {"search": query, "products": products, "product_count": get_product_count(request), "qsc": Category.objects.all()})


def allProducts(request):
    products = Product.objects.filter()
    return render(request, "allproducts.html", {"products": products, "product_count": get_product_count(request), "qsc": Category.objects.all(), "count": len(products)})


def login(request):
    r = False
    if "reg" in request.session:
        r = request.session["reg"]
    request.session["reg"] = False
    # if request.user.is_authenticated:
    #     return redirect("/")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if(user):
            auth_login(request, user)
            if 'next' not in request.GET:
                next = '/'
            else:
                next = request.GET["next"]
            print(next)
            return redirect(next)
        else:
            return render(request, "login.html", {"alert": True})
    print(r)
    return render(request, "login.html", {"alert": False, "registered": r})


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        address = request.POST.get("address")
        print(fname)
        try:
            obj = User.objects.get(email=email)
        except Exception as e:
            obj = None
        if obj is None:
            if pass1 == pass2:
                if(len(pass1)<8):
                    return render(request, "register.html",{"error":"Passsword length must be 8 characters long"})
                user = User(email=email, firstName=fname,
                            lastName=lname, address=address)
                user.set_password(pass1)
                user.save()
                request.session['reg'] = True
                return redirect("/login")
            else:
                return render(request, "register.html",{"error":"Passswords donot match"})
        else:
            return render(request, "register.html",{"error":"Email address already exixts"})

    return render(request, "register.html")



def mlogout(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/login')
def checkout(request):
    qsc = Category.objects.all()
    user = User.objects.get(pk=request.user.id)
    context = {
        "user": user
    }
    mcart = Cart.objects.filter(user=request.user)
    if len(mcart) <= 0:
        return render(request, 'cart.html', {'container': None, 'cartPrice': None, "qsc": qsc, "product_count": get_product_count(request)})
    else:
        container = Container.objects.filter(cart=mcart[0])
        totalPrice = 0
        for i in container:
            totalPrice += i.product.price*i.quantity
    return render(request, 'checkout.html', {"user": user, "qsc": qsc, 'container': container, 'cartPrice': totalPrice, "product_count": get_product_count(request)})


import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def forgetPassword(request):
    if request.method=="GET":
        email = request.GET.get("email","")
        print(email)
        if email:
            try:
                user = User.objects.get(email=email)
            except Exception as e:
                user = None
                return render(request,"verify.html",{"alert":True})#no such email exists
            s = randomString(20)
            msg = MIMEMultipart()
            msg['From'] = "me@salmanarshad.net"
            msg['To'] = email
            msg['Subject'] = "Asaan Store - Reset Password"
            message = "Please click the link below to reset your Password. If you have not requested such action Igonre this email. <br> http://40.117.251.49/forget-password?token="+s
            # add in the message body
            msg.attach(MIMEText(message, 'html'))

            # create server
            server = smtplib.SMTP('smtp-mail.outlook.com: 587')

            server.starttls()

            # Login Credentials for sending the mail
            server.login(msg['From'], "fotoalpha44&")

            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()
            UID.objects.filter(user=user).delete()
            a= UID(user=user,uid=s)
            a.save()
            return render(request,"email.html")
        token= request.GET.get("token","")
        if token!="":
            try:
                a = UID.objects.get(uid=token)
            except Exception as e:
                user = None
                return render(request,"invalid.html")#Invalid token email exists
            return render(request,"reset-password.html",{"token":token})
    return render(request,"verify.html")
def reset(request):
    if request.method=="POST":
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        token = request.POST.get("token")
        if (p1!=p1):
            return render(request, "reset-password.html",{"error":"Password do not match","token":token})
        if len(p1)<8:
            return render(request, "reset-password.html",{"error":"Password length is less than 8","token":token})
        user = UID.objects.get(uid=token).user
        user.set_password(p1)
        user.save()
        UID.objects.filter(user=user).delete()
        return redirect("/login")

            

            