from django.db import models
#from django.contrib.auth.models import User
from user.models import User
#from django.conf.settings import AUTH_USER_MODEL
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    profileImage = models.ImageField(upload_to="static/product_img")
    Description = models.TextField()
    Discount = models.PositiveIntegerField()

    def getDiscountedPrice(self):
        return str(float(self.price)-float(self.price)*(self.Discount/100))

    # 1 1 1,2,3,
    def __str__(self):
        return self.name


class singleImage(models.Model):
    image = models.ImageField(upload_to="static/product_img")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "zimageContainer"

    def __str__(self):
        return self.image.name


class Container(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
 
class UID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=250)





