import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pApp.models import quotation, depositslip, deposit_orders, slips
import json

def upload_images(request, depositslip_number):
    """ ฟังก์ชันสำหรับอัปโหลดรูปภาพและบันทึกลงในฐานข้อมูล """
    _depositslip = get_object_or_404(depositslip, depositslip_number=depositslip_number)
    file_urls = []  # เก็บ URL ของไฟล์ที่อัปโหลด

    if 'images' in request.FILES:
        for image in request.FILES.getlist('images'):
            new_slip = slips(deposit=_depositslip, slip=image)
            new_slip.save()  # บันทึกข้อมูลรูปภาพลงฐานข้อมูล
            file_urls.append(new_slip.slip.url)  # เพิ่ม URL ไฟล์เข้า list

    return file_urls
