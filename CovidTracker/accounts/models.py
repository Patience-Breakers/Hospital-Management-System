from django.db import models

# Create your models here.

class patient(models.Model):
    name = models.TextField()
    temperature = models.TextField()
    o2level= models.TextField()
    date = models.TextField()
    address = models.TextField()
    symptoms = models.TextField()
    exitingdisease =models.BooleanField()
  