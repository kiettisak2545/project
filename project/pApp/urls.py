from django.urls import path
from pApp import views
from pApp.backEnd import  form, login, profile ,signature,register,quotation,adminmanage,edit_quotation
urlpatterns = [
    path('',login.Login),
    path('Register', register.Register),
    path('index',views.index),
    path('home',views.home),
    path('showProfile',profile.showProfile),
    path('form/',form.form),
    path('signature/',signature.signature_view, name='signature'),
    path('quotation/<str:number>/edit_quotation/', edit_quotation.edit_quotation, name='edit_quotation'),
    # url ในแต่ละใบเสนอราคาที่เชิ่อมต่อไป หน้า quotation
    path('quotation/<str:quotation_number>/', quotation.quotation_view, name='quotation'),  # ใช้ฟังก์ชัน quotation_view

    #ดิ๊กเขียน
    path('adminmanage/manage/', adminmanage.adminmanage, name='quotation'),
]