import json

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from pApp.models import deposit_orders, depositslip, imgs, quotation, slips, user
       

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

        
       
        session_key = f"updated_paid_status_{_depositslip.id}"

        if not request.session.get(session_key, False):  # ถ้ายังไม่เคยทำการอัปเดต
            if _depositslip.deposit_paidstatus == "finish":
                # อัปเดตค่า paidprice และ balanceprice
                _depositslip.deposit_paidstatus = "0"
                _quotation.paidprice += _depositslip.deposit_total
                _quotation.balanceprice -= _depositslip.deposit_total
                _quotation.save()
                _depositslip.save()
                
               

                # บังคับให้โหลดค่าล่าสุดจาก DB
                _quotation.refresh_from_db()

                # บันทึกใน session เพื่อไม่ให้ทำซ้ำ
                request.session[session_key] = True
                request.session.modified = True  # บังคับให้ Django บันทึก Session


    except ImproperlyConfigured as e:
        return JsonResponse({"success": False, "error": str(e)})
    
    if request.method == "POST":
        try:
            if request.FILES.getlist('images'):
                for image in request.FILES.getlist('images'):
                    new_img = slips(deposit=_depositslip, img=image)
                    new_img.save()
                # รีเฟรช URL ของภาพหลังจากอัปโหลดใหม่
                file_urls = [img.slip.url for img in imgs.objects.filter(deposit=_depositslip)]
                return redirect(request.path)
            else:
                data = json.loads(request.body.decode('utf-8'))
                if "toggle_status" in data:
                    _depositslip.deposit_status = -1 if _depositslip.deposit_status == 0 else 0
                    _depositslip.save()
                    return JsonResponse({"success": True, "new_status": _depositslip.deposit_status})
        except Exception as e:
           return redirect(request.path)
    

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
