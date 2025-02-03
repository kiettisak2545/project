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
        for slip in depositslips:
            deposit_data.append({
                "depositslip": slip,
                "deposit_orders": deposit_orders.objects.filter(depositslip=slip),
                "state": "depositslip_" + str(slip.id)  # กำหนด state ไดนามิก
            })

        # ✅ ดึงข้อมูล user
        context_user = get_object_or_404(user, id=1)

        #task_state = quotation_data.quotation_status

        # ✅ กำหนด state หลัก
        #task_state = "quotation" if not depositslips else deposit_data[1]["state"]

        task_state = deposit_data[0]["state"]

        # ✅ ส่งข้อมูลไปยังเทมเพลต
        return render(request, 'quotation.html', {
            'task_state': task_state,
            'quotation': quotation_data,
            'orders': orders,
            'deposit_data': deposit_data,  # ✅ เก็บ depositslip & orders แยกกัน
            'user': context_user,
        })
    except quotation.DoesNotExist:
        raise Http404("Quotation not found")
