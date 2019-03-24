from django.contrib import admin
from django.urls import path, include
from contact.views import contactForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),
    path('contact/',contactForm)
]
