from django.contrib import admin
from django.urls import path, include
from contact.views import contactForm
from aboutus.views import about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),
    path('contact/',contactForm),
    path('about-us',about_us)
]
