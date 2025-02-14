from django import template
from pApp.backEnd.ulity import encrypt_url  # นำเข้าฟังก์ชัน encrypt_url ที่คุณสร้างขึ้น

register = template.Library()

@register.filter
def encrypt_quotation_number(value):
    return encrypt_url(value)
