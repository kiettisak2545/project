from django.urls import path
from pApp import views
urlpatterns = [
    path('',views.Login),
    path('Register', views.Register),
    path('ForgetPass', views.ForgetPass),
    path('Edit/<userId>',views.Edit),
    path('index',views.index),
    path('home',views.home),
    path('showProfile',views.showProfile),
    path('form',views.form)
]