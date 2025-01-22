from django.db import models
from django.urls import reverse

# Create your models here.
class user(models.Model):
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=25) 
    name = models.CharField(max_length= 25)
    lastName = models.CharField(max_length= 25)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)



from django.db import models

class quotation(models.Model):  
    number = models.CharField(max_length=10)
    url = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)

class order(models.Model):   
    amount = models.IntegerField()
    orderName = models.CharField(max_length=25)
    price = models.IntegerField()
    total = models.IntegerField()
    totalPrice = models.IntegerField()
    quotation = models.ForeignKey(
        quotation,on_delete=models.CASCADE, related_name="orders"
    )  # เพิ่ม ForeignKey เพื่อเชื่อมโยงกับ Quotation

def __str__(self):
    return "name =" + self.name


 