from django.contrib import admin
from pApp.models import user,quotation,order

# Register your models here.
admin.site.register(user)
admin.site.register(quotation)
admin.site.register(order)