from django.shortcuts import render
from pApp.models import depositslip

def depositslip(request, quotation_number):
    
    # ใช้ quotation_number เพื่อประมวลผลข้อมูล
    return render(request, 'depositslipmanage.html', {'quotation_number': quotation_number})
