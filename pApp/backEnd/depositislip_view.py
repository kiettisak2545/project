from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pApp.models import quotation, depositslip, deposit_orders, user
import json

def deposit_slip_view(request, depositslip_number):
    _depositslip = get_object_or_404(depositslip, depositslip_number=depositslip_number)
    _quotation = _depositslip.quotation
    _deposit_orders = deposit_orders.objects.filter(depositslip=_depositslip)
    context_user = get_object_or_404(user, id=1)

    # 📌 ตรวจสอบว่ามีการส่งคำขอเปลี่ยน deposit_status หรือไม่
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if "toggle_status" in data:
                _depositslip.deposit_status = -1 if _depositslip.deposit_status == 0 else 0
                _depositslip.save()
                return JsonResponse({"success": True, "new_status": _depositslip.deposit_status})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    # ถ้าไม่ใช่ POST ก็แสดงหน้า HTML ปกติ
    context = {
        "depositslip": _depositslip,
        "deposit_orders": _deposit_orders,
        "quotation": _quotation,
        "user": context_user,
    }
    
    return render(request, 'depositslip_view.html', context)
