from django.shortcuts import get_object_or_404, render
from pApp.models import quotation

def depositslip(request, quotation_number):
    quotation_data = get_object_or_404(quotation, number=quotation_number)
    depositslip_data = quotation_data.depositslip.all()  # ใช้ related_name สำหรับดึงข้อมูล
    all_quotations = quotation.objects.all()  # ดึงรายการ quotations ทั้งหมด (ปรับตามเงื่อนไข)

    return render(
        request, 
        'depositslipmanage.html', 
        {
            'quotation_number': quotation_data, 
            'depositslip': depositslip_data,
            'quotations': all_quotations  # ส่งตัวแปร quotations ไปยัง Template
        }
    )