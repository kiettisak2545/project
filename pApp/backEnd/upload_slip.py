from django.conf import settings
from django.shortcuts import render, redirect
from pApp.models import slips
import os

def upload_slip(request):
    if request.method == "POST" and request.FILES.get("slip"):
        slip_image = request.FILES["slip"]  # รับไฟล์จากฟอร์ม

        # ตรวจสอบว่าโฟลเดอร์ 'slips' ใน media มีอยู่แล้ว ถ้าไม่ให้สร้าง
        slips_dir = os.path.join(settings.MEDIA_ROOT, 'slips')
        if not os.path.exists(slips_dir):
            os.makedirs(slips_dir)

        # สร้างพาธสำหรับบันทึกไฟล์
        file_path = os.path.join(slips_dir, slip_image.name)

        # บันทึกไฟล์ลงในที่เก็บไฟล์
        with open(file_path, 'wb+') as destination:
            for chunk in slip_image.chunks():
                destination.write(chunk)

        return render(request, "upload_slip.html", {"message": "File uploaded successfully!"})

    return render(request, "quotation.html")