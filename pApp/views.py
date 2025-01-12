from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from pApp.models import user
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse

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
            login(request, user)  # หากข้อมูลถูกต้องให้ทำการล็อกอิน
            return redirect("/home")  # เมื่อเข้าสู่ระบบสำเร็จให้เปลี่ยนไปหน้า home หรือหน้าหลัก

        else:
            messages.error(request, email+password)  # หากไม่ถูกต้องจะแสดงข้อความผิดพลาด

    return render(request, "Login.html")  # ให้แสดงฟอร์มล็อกอิน


def Register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user.objects.create(
            email = email,
            password = password
        )

        #messages.success(request,"SaveData")

        return redirect("/")
    else:
        return render(request,"Register.html")

def ForgetPass(request):
    return render(request,"ForgetPass.html")

def Edit(request,userId):
    if request.method == "POST":
        _user = user.objects.get(id=userId)
        _user.name = request.POST['name']
        _user.lastName = request.POST['lastName'] 
        _user.save()

 
        return redirect("/showProfile")
    else:
        #get edit data
        _user = user.objects.get(id=userId)
        return render(request,"Edit.html",{"user":_user})
    

def index(request):
     return render(request,"index.html")

def home(request):
     return render(request,"home.html")

def showProfile(request):
     all_user = user.objects.all( )
     return render(request,"showProfile.html",{"all_user":all_user})

def form(request):
    return render(request,"form.html")