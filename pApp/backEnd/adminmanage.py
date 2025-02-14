from django.shortcuts import render
from pApp.models import quotation
from pApp.backEnd.ulity import encrypt_url  # เพิ่มการ import ฟังก์ชัน encrypt_url

def adminmanage(request):
    # ดึงข้อมูล Quotation ทั้งหมดจากฐานข้อมูล
    quotations = quotation.objects.all()

    # ส่งข้อมูลไปยัง Template พร้อมฟังก์ชัน encrypt_url
    return render(request, 'adminmanage/index.html', 
    {
        'quotations': quotations,
        'encrypt_url': encrypt_url,  # เพิ่มฟังก์ชัน encrypt_url ใน context
    })
