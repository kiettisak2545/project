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
#ข้อมูลธนาคาร
    bank = models.CharField(max_length=25)
    bank_address = models.CharField(max_length=50)
    accountnumber = models.CharField(max_length=15)
    userid_card = models.CharField(max_length=15)

class quotation(models.Model):  
    number = models.CharField(max_length=10)
    url = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)

    totalPrice = models.IntegerField()
    quotation_status = models.CharField(max_length=10)

class order(models.Model):   
    amount = models.IntegerField()
    orderName = models.CharField(max_length=25)
    price = models.IntegerField()
    total = models.IntegerField()
    quotation = models.ForeignKey(
        quotation,on_delete=models.CASCADE, related_name="orders"
    )  # เพิ่ม ForeignKey เพื่อเชื่อมโยงกับ quotation

class depositslip(models.Model):

    depositslip_number = models.CharField(max_length=25)
    depositslip_date = models.DateField(null=True, blank=True)
    deposit_total = models.IntegerField()
    deposit_vat = models.IntegerField()
    deposit_totalprice = models.IntegerField()

    deposit_status = models.IntegerField()

    quotation = models.ForeignKey(
        quotation,on_delete=models.CASCADE, related_name="depositslips"
    )  # เพิ่ม ForeignKey เพื่อเชื่อมโยงกับ depositslip
    

class deposit_orders(models.Model):
    deposit_ordername = models.CharField(max_length=25)
    deposit_price = models.IntegerField()  
    depositslip = models.ForeignKey(
        depositslip,on_delete=models.CASCADE, related_name="_deposit_order"
    )  # เพิ่ม ForeignKey เพื่อเชื่อมโยงกับ depositslip

class slips(models.Model):
    slip = models.ImageField(upload_to="slips/", null=True, blank=True) 
    deposit = models.ForeignKey(
        depositslip, on_delete=models.CASCADE, related_name="Dslips"
    )  # เชื่อมกับ depositslip

def __str__(self):
    return "name =" + self.name


 