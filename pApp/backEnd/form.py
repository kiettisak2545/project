from django.shortcuts import render, redirect
from pApp.models import quotation,order

def form(request):
    if request.method == "POST":
        row_number = 1  # เริ่มจากแถวแรก
        while True:
            # ดึงข้อมูลจากฟอร์ม
            item = request.POST.get(f"item{row_number}")
            quantity = request.POST.get(f"quantity{row_number}")
            price = request.POST.get(f"price{row_number}")

            # ตรวจสอบว่าแถวนี้มีข้อมูลหรือไม่
            if not item and not quantity and not price:
                break  # ถ้าไม่มีข้อมูลในแถวนี้ ให้หยุดลูป
            
            # สร้างวัตถุ Item และบันทึกลงในฐานข้อมูล
            quotation.objects.create(
                item=item,
                quantity=int(quantity),  # แปลงเป็น Integer
                price=float(price)  # แปลงเป็น Float (Decimal จะดีกว่าในการใช้งาน)
            )

            order.objects.create(
                item=item,
                quantity=int(quantity),  # แปลงเป็น Integer
                price=float(price)  # แปลงเป็น Float (Decimal จะดีกว่าในการใช้งาน)
            )
            
            row_number += 1  # เพิ่มตัวเลขแถวไปเรื่อยๆ

        return redirect('/order')  # เปลี่ยนไปหน้าสำเร็จ (หรือหน้าอื่นที่ต้องการ)

    return render(request, "form.html")
