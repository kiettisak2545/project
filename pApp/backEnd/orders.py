
from django.shortcuts import render
from pApp.models import order,quotation

def orders(request) :
    all_order = order.objects.all( )
    all_quotation = quotation.objects.all( )
    return render(request,"orders.html",{"all_order":all_order},{"all_quotation":all_quotation})