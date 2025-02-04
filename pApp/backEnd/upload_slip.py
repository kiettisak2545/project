from django.conf import settings
from django.shortcuts import render, redirect
from pApp.models import slips
import os

def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]  # รับไฟล์จากฟอร์ม

        # สร้างพาธสำหรับเก็บไฟล์
        file_path = os.path.join(settings.MEDIA_ROOT, "uploads", image_file.name)

        # สร้างโฟลเดอร์ uploads หากยังไม่มี
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        # บันทึกไฟล์ลงในที่เก็บไฟล์
        with open(file_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        return render(request, "quotation.html", {"message": "File uploaded successfully!"})

    return render(request, "quotation.html")