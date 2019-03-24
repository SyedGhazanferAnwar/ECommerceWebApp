from django.conf import settings
from django.db import models
from Product.models import Product
# Create your models here.

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Cartx(models.Model):
    user       = models.ForeignKey(User, null=True, blank=True, on_delete=None,related_name='user')
    products   = models.ManyToManyField(Product, blank=True)
    total      = models.FloatField(default=0.00)
    updated  = models.DateTimeField(auto_now=True)
    timestamp  = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)