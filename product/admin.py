from django.contrib import admin

# Register your models here.

from .models import Product, Category, singleImage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(singleImage)
