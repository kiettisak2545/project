from django.shortcuts import render


def depositslip_form(request):
    number = request.GET.get('number', None)  # ดึงพารามิเตอร์ 'number'
    # เพิ่ม logic ในการแสดงฟอร์มพร้อมข้อมูลที่เหมาะสม
    return render(request, 'depositslip_form.html', {'number': number})
