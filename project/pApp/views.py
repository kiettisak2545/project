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



def ForgetPass(request):
    return render(request,"auth/ForgetPass.html")

def Edit(request,userId):
    if request.method == "POST":
        _user = user.objects.get(id=userId)
        _user.name = request.POST['name']
        _user.lastName = request.POST['lastName'] 
        _user.save()

 
        return redirect("user/showProfile")
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




#ดิ๊กเขียน
def adminmanage(request):
    return render(request, 'adminmanage/index.html')