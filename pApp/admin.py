from django.contrib import admin
from pApp.models import user,quotation,order,depositslip,deposit_orders,slips

# Register your models here.
admin.site.register(user)
admin.site.register(quotation)
admin.site.register(order)
admin.site.register(depositslip)
admin.site.register(deposit_orders)
admin.site.register(slips)