import json

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from pApp.models import deposit_orders, depositslip, imgs, quotation, user


def deposit_slip_view(request, depositslip_number):
    try:
        # ดึงข้อมูล depositslip ตาม depositslip_number
        _depositslip = get_object_or_404(depositslip, depositslip_number=depositslip_number)
        _quotation = _depositslip.quotation
        _deposit_orders = deposit_orders.objects.filter(depositslip=_depositslip)
        context_user = get_object_or_404(user, id=1)
        # ดึงข้อมูลภาพจาก model imgs ที่เชื่อมโยงกับ depositslip นี้
        _imgs = imgs.objects.filter(deposit=_depositslip)
        # สร้าง list ของ URL ภาพจาก slips
        file_urls = [img.slip.url for img in _imgs]
    except ImproperlyConfigured as e:
        return JsonResponse({"success": False, "error": str(e)})
    
    if request.method == "POST":
        try:
            if request.FILES.getlist('images'):
                for image in request.FILES.getlist('images'):
                    new_img = imgs(deposit=_depositslip, slip=image)
                    new_img.save()
                # รีเฟรช URL ของภาพหลังจากอัปโหลดใหม่
                file_urls = [img.slip.url for img in imgs.objects.filter(deposit=_depositslip)]
            else:
                data = json.loads(request.body.decode('utf-8'))
                if "toggle_status" in data:
                    _depositslip.deposit_status = -1 if _depositslip.deposit_status == 0 else 0
                    _depositslip.save()
                    return JsonResponse({"success": True, "new_status": _depositslip.deposit_status})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    show_button = True
    context = {
        "depositslip": _depositslip,
        "deposit_orders": _deposit_orders,
        "quotation": _quotation,
        "user": context_user,
        "show_button": show_button,
        "file_urls": file_urls,  # ส่ง URL ภาพไปยัง template
    }
    
    return render(request, 'depositslip_view.html', context)
