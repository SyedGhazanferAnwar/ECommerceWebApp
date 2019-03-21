from django.db import models

# Create your models here.


class singleImage(models.Model):
    image = models.ImageField()

    class Meta:
        verbose_name_plural = "zimageContainer"


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
    Images = models.ForeignKey(singleImage, on_delete=models.CASCADE)
    Description = models.TextField()
    Discount = models.IntegerField()

    def __str__(self):
        return self.name
