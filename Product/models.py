from django.db import models
#from django.contrib.auth.models import User
from user.models import User
from categories.models import Category
#from django.conf.settings import AUTH_USER_MODEL
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    profileImage = models.ImageField(upload_to="static/product_img")
    Description = models.TextField()
    Discount = models.PositiveIntegerField()

    # 1 1 1,2,3,
    def __str__(self):
        return self.name


class singleImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "zimageContainer"

    def __str__(self):
        return self.image.name


class Container(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, primary_key=True)
    quantity = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.product.name+'('+str(self.quantity)+')'


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # contains one product and its quantity
    container = models.ManyToManyField(Container)

    def __str__(self):
        return self.user.firstName+' '+self.user.lastName+'(CART)'

# 1 asd asdsa 10
# bauhat sare cart mein aik product asakta hai
