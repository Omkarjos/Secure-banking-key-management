from cryptography.fernet import Fernet
from django.utils import timezone
from .models import Key

def generate_key(alias):
    return Key.objects.create(alias=alias,encrypted_material=Fernet.generate_key().decode())

def rotate_key(key):
    key.encrypted_material=Fernet.generate_key().decode()
    key.version+=1
    key.rotated_at=timezone.now()
    key.status="ACTIVE"
    key.save()
    return key

def revoke_key(key):
    key.status="REVOKED"
    key.save(update_fields=["status"])
    return key
