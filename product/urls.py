from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products', views.product, name='Product')
]
