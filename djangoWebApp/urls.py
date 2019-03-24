from django.contrib import admin
from django.urls import path, include
from contact.views import contactForm
from cart.views import cart_home
from .views import homepage

urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),
    path('contact/',contactForm),
    #Custom cart currently being worked on
    path('cartx/',cart_home)
]
