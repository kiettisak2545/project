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
    
    #taks
    url = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    
    #quotation
    number = models.CharField(max_length=10)
    vat = models.IntegerField()
    totalPrice = models.IntegerField() #จำนวนทั้งหมด
    total = models.IntegerField()#จำนวนทั้งหมดร่วมภาษี

    #status
    chargedprice = models.IntegerField() # จำนวนเรียกเก็บ
    paidprice = models.IntegerField() #จำนวนที่จ่ายแล้ว
    balanceprice = models.IntegerField() # จำนวนเงินคงเหลือ
    deposit_total = models.IntegerField() # จำนวนสร้างใบโอนเรียกเก็บทั้งหมด
    quotation_status = models.CharField(max_length=10)

    n = models.IntegerField()


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
    
    deposit_status = models.IntegerField()
    deposit_paidstatus = models.CharField(max_length=25) # สถานะจ่ายเงินแล้ว

    num = models.IntegerField()


    

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
    img = models.ImageField(upload_to="img/", null=True, blank=True) 
    
    deposit = models.ForeignKey(
        depositslip, on_delete=models.CASCADE, related_name="Dslips"
    )  # เชื่อมกับ depositslip

class imgs(models.Model):
    slip = models.ImageField(upload_to="slips/", null=True, blank=True) 
    
    deposit = models.ForeignKey(
        depositslip, on_delete=models.CASCADE, related_name="Dimg"
    )  # เชื่อมกับ depositslip

class review(models.Model) :
    star = models.IntegerField()
    comment = models.CharField(max_length=250)
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

 

def __str__(self):
    return "name =" + self.name


 