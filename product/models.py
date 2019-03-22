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
    rating = models.FloatField()
    price = models.FloatField()
    stock = models.IntegerField()
    profileImage = models.ImageField()
    Description = models.TextField()
    Discount = models.IntegerField()

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


class Cart(models.Model):
    _user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    models.ManyToManyField(Product)

# 1 asd asdsa 10
# bauhat sare cart mein aik product asakta hai