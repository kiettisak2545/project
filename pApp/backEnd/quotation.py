from django.http import Http404
from django.shortcuts import render, get_object_or_404
from pApp.models import quotation, order, depositslip, deposit_orders, user

def quotation_view(request, quotation_number):
    try:
        # ✅ ดึงข้อมูล Quotation จากฐานข้อมูล
        quotation_data = get_object_or_404(quotation, number=quotation_number)
        
        # ✅ ดึงข้อมูล orders ที่เกี่ยวข้อง
        orders = order.objects.filter(quotation=quotation_data)

        # ✅ ดึงข้อมูล depositslips ที่สัมพันธ์กับ Quotation
        depositslips = depositslip.objects.filter(quotation=quotation_data).prefetch_related("_deposit_order")

        # ✅ สร้าง Dict สำหรับแยก State
        deposit_data = []
        deposit_state = None  # กำหนดค่าเริ่มต้น

        for slip in depositslips:
            deposit_status = slip.deposit_status
            # ✅ ตรวจสอบว่า deposit_status มีค่า 0 หรือ -1 เท่านั้น
            if deposit_status != 0 and deposit_status != -1:
                deposit_status = 0  # ถ้าไม่ใช่ 0 หรือ -1 ให้ใช้ 0

            deposit_data.append({
                "depositslip": slip,
                "deposit_orders": deposit_orders.objects.filter(depositslip=slip),
                "state": deposit_status
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

        context = {
            'task_state': deposit_state,  # ✅ task_state จะสัมพันธ์กับ deposit_status ล่าสุด
            'quotation': quotation_data,
            'orders': orders,
            'deposit_data': deposit_data,  # ✅ เก็บ depositslip & orders แยกกัน
            'user': context_user,
            'quotation_state': quotation_state,
            'steps': steps,  # เพิ่มขั้นตอนการแสดงสถานะทั้งหมด
            'deposit_per_step': deposit_per_step,  # เปอร์เซ็นต์ของการโอนมัดจำ
            'depositslips': depositslips,  # ส่งข้อมูล depositslips ไปยังเทมเพลต
        }

        # ✅ ส่งข้อมูลไปยังเทมเพลต
        return render(request, 'quotation.html', context)
    except quotation.DoesNotExist:
        raise Http404("Quotation not found")
