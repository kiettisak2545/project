from django.contrib import admin

from pApp.models import (deposit_orders, depositslip, imgs, order, quotation,
                         slips, user,review)

# Register your models here.
admin.site.register(user)
admin.site.register(quotation)
admin.site.register(order)
admin.site.register(depositslip)
admin.site.register(deposit_orders)
admin.site.register(slips)
admin.site.register(imgs)
admin.site.register(review)