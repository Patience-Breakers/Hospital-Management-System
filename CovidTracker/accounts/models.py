from django.db import models

# Create your models here.

class patient(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10) # M of F 
    temperature = models.TextField()
    o2level= models.TextField()
    date = models.TextField()
    address = models.TextField()
    symptoms = models.TextField()
    exitingdisease =models.TextField()
    status = models.CharField
    ## Recovered ,Admitted or Decreased
  