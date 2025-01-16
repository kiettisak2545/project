from django.urls import path
from pApp import views
from pApp.backEnd import edit, form, login, profile ,signature,orders,register
urlpatterns = [
    path('',login.Login),
    path('Register', register.Register),
    path('ForgetPass', views.ForgetPass),
    path('Edit/<userId>',edit.Edit),
    path('index',views.index),
    path('home',views.home),
    path('showProfile',profile.showProfile),
    path('form/',form.form),
    path('orders',orders.orders),
    path('signature/',signature.signature_view, name='signature'),


    #ดิ๊กเขียน
    path('adminmanage/manage/', views.adminmanage, name='admin_manage'),
]