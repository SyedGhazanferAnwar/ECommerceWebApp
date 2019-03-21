from django.db import models

# Create your models here.


class product(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    rating = models.FloatField()
    price = models.FloatField()
    stock =models.IntegerField()
    profileImage =models.ImageField()
    Images =models
    # Description =
    # Discount =
    # Reviews =
    # body = models.TextField()

class Business(models.Model):
    singleImage=models.ImageField()