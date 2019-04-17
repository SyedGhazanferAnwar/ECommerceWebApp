from django.db import models

# Create your models here.
class Message(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100)
    message = models.CharField(max_length = 5000)

    def __str__(self):
        return self.subject