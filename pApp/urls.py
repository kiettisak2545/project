from django.urls import path
from pApp import views
from pApp.backEnd import edit, login, profile
urlpatterns = [
    path('',login.Login),
    path('Register', views.Register),
    path('ForgetPass', views.ForgetPass),
    path('Edit/<userId>',edit.Edit),
    path('index',views.index),
    path('home',views.home),
    path('showProfile',profile.showProfile),
    path('form',views.form)
]