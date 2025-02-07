from django.shortcuts import render
from django.http import HttpResponse
import base64
from io import BytesIO
from PIL import Image

def signature_view(request):
    if request.method == "POST":
        signature_data = request.POST.get('signature_data')
        if signature_data:
            # ลบ prefix 'data:image/png;base64,' ออก
            signature_data = signature_data.split(',')[1]
            # แปลงจาก base64 เป็น Image
            img_data = base64.b64decode(signature_data)
            image = Image.open(BytesIO(img_data))

            # บันทึกภาพลงในไฟล์
            image.save("signature.png")
            
            return HttpResponse("Signature saved successfully!")

    return render(request, "signature.html")
