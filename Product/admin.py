from django.contrib import admin

# Register your models here.

from .models import Product, Category, singleImage, Cart, Container,UID

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(singleImage)
admin.site.register(Cart)
admin.site.register(Container)
admin.site.register(UID)