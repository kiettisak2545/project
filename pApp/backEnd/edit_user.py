from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from pApp.models import user  # ตรวจสอบว่าโมเดลชื่อ `user` ถูกต้อง

def edit_user(request, user_id):
    # ดึงข้อมูลผู้ใช้จากฐานข้อมูล
    _user = get_object_or_404(user, id=user_id)

    if request.method == "POST":
        # รับค่าจากฟอร์มและอัปเดตข้อมูล
        _user.name = request.POST.get('name')
        _user.lastName = request.POST.get('lastName')
        _user.email = request.POST.get('email')
        _user.tel = request.POST.get('tel')
        _user.address = request.POST.get('address')
        _user.save()

        # แจ้งเตือนเมื่ออัปเดตสำเร็จ
        messages.success(request, "ข้อมูลผู้ใช้ถูกอัปเดตเรียบร้อยแล้ว!")
        return redirect('/showProfile')  # เปลี่ยนเป็นชื่อ URL หรือหน้าที่ต้องการ

    context = {
        'user': _user,  # ส่ง `_user` ที่ดึงมาจากฐานข้อมูลไปยัง Template
    }
    return render(request, 'edit_user.html', context)
