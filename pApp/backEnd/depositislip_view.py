from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ImproperlyConfigured
from pApp.models import quotation, depositslip, deposit_orders, user, slips
import json

def deposit_slip_view(request, depositslip_number):
    try:
        _depositslip = get_object_or_404(depositslip, depositslip_number=depositslip_number)
        _quotation = _depositslip.quotation
        _deposit_orders = deposit_orders.objects.filter(depositslip=_depositslip)
        context_user = get_object_or_404(user, id=1)
        _slips = slips.objects.filter(deposit=_depositslip)
        file_urls = [slip.img.url for slip in _slips]
    except ImproperlyConfigured as e:
        return JsonResponse({"success": False, "error": str(e)})
    
    if request.method == "POST":
        try:
            if request.FILES.getlist('images'):
                for image in request.FILES.getlist('images'):
                    new_slip = slips(deposit=_depositslip, img=image)
                    new_slip.save()
                file_urls = [slip.img.url for slip in slips.objects.filter(deposit=_depositslip)]
            else:
                data = json.loads(request.body.decode('utf-8'))
                if "toggle_status" in data:
                    _depositslip.deposit_status = -1 if _depositslip.deposit_status == 0 else 0
                    _depositslip.save()
                    return JsonResponse({"success": True, "new_status": _depositslip.deposit_status})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    show_button = True
    context = {
        "depositslip": _depositslip,
        "deposit_orders": _deposit_orders,
        "quotation": _quotation,
        "user": context_user,
        "show_button": show_button,
        "file_urls": file_urls,
    }
    
    return render(request, 'depositslip_view.html', context)
