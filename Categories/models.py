from django.db import models

# Create your models here.
class Category(models.Model):
	Category_title=models.CharField(max_length=200)
	description = models.TextField()

def __str__(self):
        return self.Category_title  