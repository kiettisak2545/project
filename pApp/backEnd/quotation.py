from django.conf import settings  # เพิ่มการใช้ settings
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from pApp.models import (deposit_orders, depositslip, imgs, order, quotation,
                         slips, user)


def quotation_view(request, quotation_number):
    try:
        # ✅ ดึงข้อมูล Quotation จากฐานข้อมูล
        quotation_data = get_object_or_404(quotation, number=quotation_number)
        
        # ✅ ดึงข้อมูล orders ที่เกี่ยวข้อง
        orders = order.objects.filter(quotation=quotation_data)

        # ✅ ดึงข้อมูล depositslip ที่สัมพันธ์กับ Quotation
        depositslips = depositslip.objects.filter(quotation=quotation_data)

        # ✅ สร้าง Dict สำหรับแยก State และดึง img จาก slips
        deposit_data = []
        deposit_state = None  # กำหนดค่าเริ่มต้น

        for slip in depositslips:
            deposit_status = slip.deposit_status
            # ✅ ตรวจสอบว่า deposit_status มีค่า 0 หรือ -1 เท่านั้น
            if deposit_status != 0 and deposit_status != -1:
                deposit_status = 0  # ถ้าไม่ใช่ 0 หรือ -1 ให้ใช้ 0

            # ดึงเฉพาะฟิลด์ img ของ slips ที่สัมพันธ์กับ depositslip
            slip_images = slips.objects.filter(deposit=slip).values_list('img', flat=True)
            
            # เพิ่ม MEDIA_URL เข้าไปในแต่ละ URL ของภาพ
            slip_images = [settings.MEDIA_URL + img for img in slip_images]

            deposit_data.append({
                "depositslip": slip,
                "deposit_orders": deposit_orders.objects.filter(depositslip=slip),
                "state": deposit_status,
                "image_urls": slip_images  # ส่งเฉพาะ img ของ slips
            })

        # ✅ ถ้ามี depositslip ให้ใช้ deposit_status ของอันล่าสุดเป็น task_state
        if depositslips.exists():
            latest_status = depositslips.latest('id').deposit_status
            deposit_state = latest_status if latest_status in [0, -1] else 0
        else:
            deposit_state = 0  # ถ้ายังไม่มี depositslip ให้ state เป็น 0

        # ✅ ดึงข้อมูล user
        context_user = get_object_or_404(user, id=1)

        # ✅ สถานะของใบเสนอราคา
        quotation_state = quotation_data.quotation_status
        
        # ✅ คำนวณจำนวนงวดของ depositslips
        total_deposit_slips = len(depositslips)
        deposit_per_step = 100 / total_deposit_slips if total_deposit_slips > 0 else 0  # หารตามจำนวนงวด

        # ✅ สร้างขั้นตอนทั้งหมดรวมถึงใบเสนอราคา
        steps = ['ใบเสนอราคา', 'รอโอนมัดจำ', 'โอนมัดจำแล้ว', 'ดำเนินการเสร็จสิ้น']

        # ตรวจสอบว่ามีการอัพโหลดไฟล์ภาพใหม่หรือไม่
        if request.method == 'POST' and 'slip_image' in request.FILES:
            slip_image = request.FILES['slip_image']
            deposit_number = request.POST.get('depositslip_number')  # ดึง depositslip_number จากฟอร์ม
            
            # เชื่อมโยงกับ depositslip
            depositslip_data = get_object_or_404(depositslip, depositslip_number=deposit_number)

            # สร้างบันทึกใหม่ใน model imgs โดยไม่ลบภาพเก่าที่มีอยู่
            new_img = imgs.objects.create(
                slip=slip_image,  # อัพโหลดภาพใหม่
                deposit=depositslip_data  # เชื่อมโยงกับ depositslip
            )

        context = {
            'task_state': deposit_state,
            'quotation': quotation_data,
            'orders': orders,
            'deposit_data': deposit_data,
            'user': context_user,
            'quotation_state': quotation_state,
            'steps': steps,
            'deposit_per_step': deposit_per_step,
            'depositslips': depositslips,
        }

        return render(request, 'quotation.html', context)
    except quotation.DoesNotExist:
        raise Http404("Quotation not found")
