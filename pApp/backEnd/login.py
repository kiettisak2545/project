from pyexpat.errors import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render


def authenticate_by_email(email, password):
    try:
        user = get_user_model().objects.get(email=email)
        if user.check_password(password):
            return user  # ถ้ารหัสผ่านถูกต้อง ให้คืนค่าผู้ใช้
    except get_user_model().DoesNotExist:
        return None  # ถ้าไม่พบผู้ใช้
    return None


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')  # รับค่าอีเมลจากฟอร์ม
        password = request.POST.get('password')  # รับค่ารหัสผ่านจากฟอร์ม

    
        # ตรวจสอบว่าอีเมลและรหัสผ่านถูกต้องหรือไม่
        user = authenticate_by_email(email, password)


        if user is not None:
            Login(request, user)  # หากข้อมูลถูกต้องให้ทำการล็อกอิน
            return redirect("/home")  # เมื่อเข้าสู่ระบบสำเร็จให้เปลี่ยนไปหน้า home หรือหน้าหลัก

        else:
            messages.error(request, email+password)  # หากไม่ถูกต้องจะแสดงข้อความผิดพลาด

    return render(request, "auth/Login.html")  # ให้แสดงฟอร์มล็อกอิน