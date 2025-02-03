from django.shortcuts import render, redirect
from pApp.backEnd.forms import SlipForm
from pApp.models import slips

def upload_slip(request):
    if request.method == "POST":
        print(request.FILES)  # ตรวจสอบว่ามีไฟล์ถูกส่งมาหรือไม่
        form = SlipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_slips")  # ไปยังหน้าที่แสดงภาพ
    else:
        form = SlipForm()

    return render(request, "upload_slip.html", {"form": form})
