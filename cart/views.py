from django.shortcuts import render
from .models import Cartx
# Create your views here.

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cartx.objects.filter(id=cart_id)
    if qs.count() == 1:
        print('Cart Id exists')
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cartx.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id
    return render(request, "play_cart.html", {})

#~/AHussam/