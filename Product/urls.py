from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('product/<id>', views.product, name='product'),
    path('product/<id>/addtocart/<quantity>', views.addtocart, name='Product'),
    path('cart', views.cart, name='cart')
]
