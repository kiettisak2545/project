import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_multiple_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # กำหนดให้บันทึกไฟล์ที่ media/
        for image in request.FILES.getlist('images'):  # วนลูปรับไฟล์ทั้งหมด
            fs.save(f'img/{image.name}', image)  # บันทึกไฟล์แต่ละอัน

    # ดึงรายชื่อไฟล์ทั้งหมดใน media/img/
    image_dir = os.path.join(settings.MEDIA_ROOT, 'img')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)  # สร้างโฟลเดอร์ถ้ายังไม่มี

    file_list = os.listdir(image_dir)  # ดึงชื่อไฟล์ทั้งหมด
    file_urls = [settings.MEDIA_URL + 'img/' + file for file in file_list]  # แปลงเป็น URL

    return render(request, 'upload.html', {'file_urls': file_urls})
