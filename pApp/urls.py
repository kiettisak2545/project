from django.urls import path
from pApp import views
from pApp.backEnd import  form, login, profile ,signature,register,quotation,adminmanage,edit_quotation,edit_user,depositslipmanage,depositslip_form,depositislip_view,quotation_view
urlpatterns = [
    #เข้าสู่ระบบ
    path('',login.Login),
    #สมัคร
    path('Register', register.Register),
    path('index/<str:quotation_number>/',views.index),
    path('home',views.home),
    #แสดงข้อมูลช่าง
    path('showProfile',profile.showProfile),
    #แก้ไขข้อมูลช่าง
    path('edit_user/<int:user_id>/', edit_user.edit_user, name='edit_user'),
    #หน้าสร้างใบเสนอราคา
    path('form/',form.form),
    #หน้าลงลายมือชื่อ
    path('signature/',signature.signature_view, name='signature'),
    #หน้าแก้ไขข้อมูลใบเสนอราคา
    path('quotation/<str:number>/edit_quotation/', edit_quotation.edit_quotation, name='edit_quotation'),
    # url ในแต่ละใบเสนอราคาที่เชิ่อมต่อไป หน้า quotation
    path('quotation/<str:quotation_number>/', quotation.quotation_view, name='quotation'),

    path('quotation_view/<str:quotation_number>/', quotation_view.quotation_view, name='quotation_view'),  # ใช้ฟังก์ชัน quotation_view
    #ดิ๊กเขียน หน้าสร้างและจัดการงาน
    path('adminmanage/manage/', adminmanage.adminmanage, name='quotation'),
    #หน้ารายการใบโอนมัดจำ
    path('depositslipmanage/<str:quotation_number>/', depositslipmanage.depositslip, name='depositslipmanage'),
    #ฟร์อมสร้างใบโอนมัดจำ
    path('depositslip_form/<str:quotation_number>', depositslip_form.depositslip_form, name='depositslip_form'),
    #แสดงข้อมูลใบโอนมัดจำ
    path('depositslip_view/<str:quotation_number>/<str:depositslip_number>/',depositislip_view.deposit_slip_view, name='deposit_slip_view'),


]