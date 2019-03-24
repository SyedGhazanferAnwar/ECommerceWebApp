from django.urls import path, include
from . import views
urlpatterns = [
    path('product/<id>', views.product, name='Product'),
    path('product/<id>/addtocart/<quantity>', views.addtocart, name='Product'),
    path('cart', views.cart, name='cart')
]
