from django.shortcuts import render, get_object_or_404
from pApp.models import quotation, depositslip, deposit_orders, user

def deposit_slip_view(request, depositslip_number):
    # ดึงข้อมูล DepositSlip ตาม depositslip_number
    _depositslip = get_object_or_404(depositslip, depositslip_number=depositslip_number)
    
    # ดึงข้อมูล Quotation ที่เกี่ยวข้อง
    _quotation = _depositslip.quotation
    
    # ดึงรายการ DepositOrder ที่เกี่ยวข้องกับ DepositSlip
    _deposit_orders = deposit_orders.objects.filter(depositslip=_depositslip)
    
    # ดึงข้อมูล User โดยตรงจากฐานข้อมูล (สมมติว่าต้องการ user id=1)
    context_user = get_object_or_404(user, id=1)  # แก้ไข id เป็นค่าที่คุณต้องการ

    # Context สำหรับ template
    context = {
        "depositslip": _depositslip,
        "deposit_orders": _deposit_orders,
        "quotation": _quotation,
        "user": context_user,
    }
    
    return render(request, 'depositslip_view.html', context)
