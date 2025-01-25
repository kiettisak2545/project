from django.shortcuts import render, get_object_or_404
from pApp.models import quotation  # เปลี่ยนตามชื่อโมเดลของคุณ
from django.http import Http404

def quotation_view(request, quotation_number):
    try:
        # ดึงข้อมูล Quotation จากฐานข้อมูล โดยใช้หมายเลข quotation_number
        quotation_data = get_object_or_404(quotation, number=quotation_number)
        
        # กำหนด task_state สำหรับแสดงส่วนที่ต้องการ
        task_state = 'quotation'  # หรือ 'depositslip' ขึ้นอยู่กับสถานะที่ต้องการแสดง

        # ส่งข้อมูลไปยังเทมเพลต
        return render(request, 'quotation.html', {
            'task_state': task_state,
            'quotation': quotation_data,
        })
    except quotation.DoesNotExist:
        # หากไม่พบ Quotation ที่ตรงกับหมายเลข
        raise Http404("Quotation not found")
