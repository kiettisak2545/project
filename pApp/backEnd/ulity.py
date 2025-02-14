import base64
import hashlib
from cryptography.fernet import Fernet
from django.conf import settings
from urllib.parse import quote_plus, unquote_plus
from functools import lru_cache

# 🔑 สร้างคีย์เข้ารหัสจาก SECRET_KEY โดยใช้ SHA256 และแคชไว้
@lru_cache(maxsize=1)
def generate_key():
    key_material = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    return base64.urlsafe_b64encode(key_material)

fernet = Fernet(generate_key())

# 🔐 ฟังก์ชันเข้ารหัส (พร้อม URL encoding)
def encrypt_url(value: str) -> str:
    encrypted = fernet.encrypt(value.encode()).decode()
    return quote_plus(encrypted)

# 🔓 ฟังก์ชันถอดรหัส (พร้อมการจัดการข้อผิดพลาด)
def decrypt_url(encrypted_value: str) -> str:
    try:
        decoded_value = unquote_plus(encrypted_value)
        return fernet.decrypt(decoded_value.encode()).decode()
    except Exception as e:
        return f"Decryption error: {str(e)}"  # หรือ raise Exception ถ้าต้องการให้แจ้งเตือนจริงจัง
