from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25) 
    name = models.CharField(max_length= 25)
    lastName = models.CharField(max_length= 25)


class quotation(models.Model):
    url = models.CharField(max_length=30)
    date = models.DateField()
    name = models.CharField(max_length= 25)
    lastName = models.CharField(max_length= 25)
    address = models.CharField(max_length= 50)

    
class order(models.Model):
    amount = models.IntegerField()
    odername = models.CharField(max_length=25)
    price = models.IntegerField()
    total1 = models.IntegerField()
    totalPrice = models.IntegerField()


def __str__(self):
    return "name =" + self.name


 