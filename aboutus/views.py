from django.shortcuts import render, redirect
from newsletter.views import newsletter_signup_home
from Product.models import *


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


def our_story(request):
    form = newsletter_signup_home(request)
    return render(request, "aboutus.html", {"form": form, "product_count": get_product_count(request), "qsc": Category.objects.all()})


def our_story_redirect(request):
    return redirect('/about/our-story')
