from django.db import models

# Create your models here.
class Message(models.Model):
    firstName = models.CharField(max_length = 50,blank=True)
    lastName = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50,blank=True)
    subject = models.CharField(max_length = 100,blank=True)
    message = models.CharField(max_length = 5000,blank=True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.subject