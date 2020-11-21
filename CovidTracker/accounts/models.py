from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class patient(models.Model):
    name = models.TextField()


    name = models.TextField()
    photo = models.ImageField( upload_to='pics')
    age = models.IntegerField()
    gender = models.CharField(max_length=10) # M of F 
    phone = models.IntegerField
    address = models.TextField
    emailId = models.EmailField(max_length=254)
    date = models.DateField( auto_now=False, auto_now_add=False)

    #Hospital

    bedNo = models.IntegerField()
    floor = models.IntegerField()
    o2level = models.IntegerField()
    asymptomatic = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    apetiteLoss = models.BooleanField()
    temperature = models.IntegerField()
    status = models.CharField(max_length=20)
    # admitted , recovered , decreased

    onVentilator = models.BooleanField(default=False)


    thirdastCOvidResult = models.BooleanField(default=True)
    secondlastCovidResult = models.BooleanField(default=True)
    lastCovidResult = models.BooleanField(default=True)#true for covid positive

    #If(all three are false)

    daysAdmitted = models.IntegerField()
    doctorId = models.IntegerField()
    