from datetime import datetime
from django.shortcuts import redirect, render
from django.urls import reverse
from pApp.models import order, quotation
from pApp.backEnd.ulity import encrypt_url, decrypt_url  # ✅ ใช้ฟังก์ชันเข้ารหัสจาก utility.py

def form(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        lastname = request.POST.get('lastName', '').strip()
        address = request.POST.get('address', '').strip()
        tel = request.POST.get('tel', '').strip()

        if not name or not lastname or not address or not tel:
            return render(request, "form.html", {"error": "กรุณากรอกข้อมูลให้ครบถ้วน"})

        # ✅ สร้างหมายเลข Quotation
        current_date = datetime.now()
        date_str = current_date.strftime("%Y%m%d")
        quotation_number = date_str + str(quotation.objects.count() + 1)

        # ✅ บันทึกข้อมูล Quotation
        new_quotation = quotation.objects.create(
            date=current_date,
            number=quotation_number,
            name=name,
            lastName=lastname,
            address=address,
            tel=tel,
            totalPrice=0,
            vat=0,
            total=0,
            chargedprice=0,
            paidprice=0,
            balanceprice=0,
            deposit_total=0,
            n = 1,
        )

        # ✅ เข้ารหัส Quotation Number
        encrypted_quotation_number = encrypt_url(quotation_number)

        # ✅ สร้างลิงก์ที่เข้ารหัส
        quotation_url = reverse('quotation', kwargs={'encrypted_quotation_number': encrypted_quotation_number})
        quotation_view_url = reverse('quotation_view', kwargs={'encrypted_quotation_number': encrypted_quotation_number})

        # ✅ บันทึก URL ลงใน Quotation
        new_quotation.url = quotation_url
        new_quotation.quotation_view_url = quotation_view_url
        new_quotation.quotation_status = "quotation"
        new_quotation.save()

        # ✅ สร้าง Orders
        create_orders(request, quotation_number)

        # ✅ ส่ง URL ที่เข้ารหัสไปยังหน้า Form
        return render(request, "form.html", {"success": True, "quotation_view_url": quotation_view_url})

    return render(request, "form.html")


def create_orders(request, quotation_number):
    # ✅ รับข้อมูลจากฟอร์ม
    order_names = request.POST.getlist('order_names', [])
    amounts = request.POST.getlist('amounts', [])
    prices = request.POST.getlist('prices', [])

    try:
        # ✅ ค้นหา Quotation
        related_quotation = quotation.objects.get(number=quotation_number)
        
        total_price_sum = 0  # สำหรับคำนวณผลรวมของ total

        # ✅ สร้าง Orders
        for i in range(len(order_names)):
            amount = int(amounts[i]) if amounts[i].isdigit() else 0
            price = int(prices[i]) if prices[i].isdigit() else 0
            total = amount * price
            total_price_sum += total  # รวม total ของแต่ละ order

            # ✅ บันทึก Order
            order.objects.create(
                quotation=related_quotation,
                orderName=order_names[i].strip(),
                amount=amount,
                price=price,
                total=total,
            )

        # ✅ อัปเดตยอดรวมของ Quotation
        related_quotation.vat = total_price_sum * 0.07
        related_quotation.total = total_price_sum * 1.07
        related_quotation.chargedprice = total_price_sum * 1.07  # จำนวนที่ต้องจ่าย
        related_quotation.balanceprice = total_price_sum * 1.07  # จำนวนทั้งหมด
        related_quotation.totalPrice = total_price_sum
        related_quotation.save()  # ✅ บันทึกข้อมูล

        return redirect("/adminmanage/manage")  # ✅ กลับไปหน้าจัดการคำสั่งซื้อ
    except quotation.DoesNotExist:
        return render(request, "form.html")
