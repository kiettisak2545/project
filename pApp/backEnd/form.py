from django.shortcuts import redirect, render

from pApp.models import order, quotation


def form(request):
    if request.method == "POST":
        # quotation
        date = request.POST["date"]
        name = request.POST["name"]
        lastName = request.POST["lastname"]
        address = request.POST["address"]
        #order
        amount = request.POST["amount"]
        orderName = request.POST["odrename"]
        price = request.POST["price"]
        total = request.POST["total"]
        totalPrice = request.POST["totalprice"]
       
        quotation.objects.create(
            date = date,
            name = name,
            lastName = lastName,
            address = address
        ) # เซพอัตโนมัติ

        order.objects.create(
            amount = amount,
            orderName = orderName,
            price = price,
            total = total,
            totalPrice = totalPrice
        )  # เซพอัตโนมัติ

        #messages.success(request,"SaveData")

        return redirect("/form")
    else:
         return render(request,"form.html")
