from django.shortcuts import get_object_or_404, render
from pApp.backEnd.ulity import decrypt_url  # นำเข้าฟังก์ชัน decrypt_url
from pApp.models import quotation  # import โมเดลที่ชื่อ quotation

def quotation_view(request, encrypted_quotation_number):
    # ถอดรหัส quotation_number ที่ได้รับมา
    quotation_number = decrypt_url(encrypted_quotation_number)

    # ดึงข้อมูล Quotation จากฐานข้อมูล
    quotation_data = get_object_or_404(quotation, number=quotation_number)
    
    # ดึงข้อมูล Order ที่เชื่อมโยงกับ Quotation
    orders = quotation_data.orders.all()  # ใช้ related_name สำหรับดึง orders

    # ส่งข้อมูลไปยัง Template
    return render(request, 'quotation_view.html', 
    {
        'quotation': quotation_data, 
        'orders': orders,
        'show_button': True  # กำหนดให้แสดงปุ่มเฉพาะที่หน้า quotation_view
    })
