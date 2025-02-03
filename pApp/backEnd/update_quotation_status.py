from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from pApp.models import quotation

@csrf_exempt  # ปิดการตรวจสอบ CSRF (ควรใช้ CSRF Token ถ้าเป็น Production)
def update_quotation_status(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            quotation_number = data.get("quotation_number")
            new_status = data.get("status")

            # ค้นหา Quotation
            quotation_data = get_object_or_404(quotation, number=quotation_number)
            quotation_data.quotation_status = new_status
            quotation_data.save()

            return JsonResponse({"success": True, "new_status": new_status})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
    
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
