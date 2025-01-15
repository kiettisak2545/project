from django.shortcuts import render, redirect
from pApp.models import quotation,order



def form(request):
    if request.method == "POST":
        
        name = request.POST['nsme']
        lastname = request.POST['lastName']
        address = request.POST['address']
        tel = request.POST['tel']

        quotation.objects.create(
            name = name,
            lastName = lastname,
            address = address,
            tel = tel
        )

        row_number = 1  # เริ่มจากแถวแรก
        while True:
            # ดึงข้อมูลจากฟอร์ม
            amount = request.POST.get(f"amount{row_number}") 
            ordername = request.POST.get(f"oderName{row_number}")
            price = request.POST.get(f"price{row_number}")

            # ตรวจสอบว่าแถวนี้มีข้อมูลหรือไม่
            if not amount and not ordername and not price:
                break  # ถ้าไม่มีข้อมูลในแถวนี้ ให้หยุดลูป
            
            # สร้างวัตถุ และบันทึกลงในฐานข้อมูล
        
            order.objects.create(
                amount = amount,
                orderName = ordername,
                price = price
            )
            
            row_number += 1  # เพิ่มตัวเลขแถวไปเรื่อยๆ

        return redirect('/order')  # เปลี่ยนไปหน้าสำเร็จ (หรือหน้าอื่นที่ต้องการ)

    return render(request, "form.html")
