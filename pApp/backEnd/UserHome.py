from django.shortcuts import render
from pApp.models import user, review  # นำเข้า model user และ review

def UserHome(request):
    # ดึงข้อมูล User ทั้งหมดจากฐานข้อมูล
    users = user.objects.all()

    # ดึงข้อมูลรีวิวทั้งหมดจากฐานข้อมูล
    reviews = review.objects.all()

    # ส่งข้อมูลไปยัง Template
    return render(request, 'UserHome.html', {'users': users, 'reviews': reviews})
