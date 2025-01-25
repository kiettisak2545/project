from django.shortcuts import render, redirect
from pApp.models import depositslip, deposit_orders


def depositslip_form(request):
    number = request.GET.get('number', None)  # ดึงพารามิเตอร์ 'number'

    if request.method == 'POST':
        # ดึงค่าจากฟอร์ม
        depositslip_number = request.POST.get('depositslip_number')
        depositslip_date = request.POST.get('depositslip_date')
        deposit_total = request.POST.get('deposit_total')
        deposit_vat = request.POST.get('deposit_vat')
        deposit_totalprice = request.POST.get('deposit_totalprice')
        deposit_totalpriceTH = request.POST.get('deposit_totalpriceTH')
        deposit_status = request.POST.get('deposit_status', 'Pending')  # กำหนดค่าเริ่มต้น

        # สร้าง depositslip ใหม่และบันทึกลงฐานข้อมูล
        new_deposit = depositslip.objects.create(
            depositslip_number=depositslip_number,
            depositslip_date=depositslip_date,
            deposit_total=deposit_total,
            deposit_vat=deposit_vat,
            deposit_totalprice=deposit_totalprice,
            deposit_totalpriceTH=deposit_totalpriceTH,
            deposit_status=deposit_status,
        )

        # ดึงรายการสั่งซื้อจากฟอร์ม
        deposit_ordername = request.POST.getlist('deposit_ordername')
        deposit_price = request.POST.getlist('deposit_price')

        # สร้าง deposit_orders ใหม่ที่เชื่อมโยงกับ depositslip
        for name, price in zip(deposit_ordername, deposit_price):
            deposit_orders.objects.create(
                deposit_ordername=name,
                deposit_price=price,
                depositslip=new_deposit,
            )

        return redirect('/depositslipmanage')  # เปลี่ยนเส้นทางเมื่อบันทึกสำเร็จ

    return render(request, 'depositslip_form.html', {'number': number})
