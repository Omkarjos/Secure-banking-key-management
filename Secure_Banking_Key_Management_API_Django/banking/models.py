from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Key(models.Model):
    STATUS=[("ACTIVE","ACTIVE"),("REVOKED","REVOKED")]
    alias=models.CharField(max_length=120,unique=True)
    algorithm=models.CharField(max_length=80,default="Fernet-demo")
    version=models.PositiveIntegerField(default=1)
    status=models.CharField(max_length=20,choices=STATUS,default="ACTIVE")
    encrypted_material=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    rotated_at=models.DateTimeField(null=True,blank=True)
    def __str__(self): return f"{self.alias} v{self.version}"

class Certificate(models.Model):
    common_name=models.CharField(max_length=200)
    serial_number=models.CharField(max_length=100,unique=True)
    issued_at=models.DateTimeField(default=timezone.now)
    expires_at=models.DateTimeField()
    status=models.CharField(max_length=30,default="ACTIVE")

class Transaction(models.Model):
    reference=models.CharField(max_length=60,unique=True)
    customer_id=models.CharField(max_length=80)
    amount=models.DecimalField(max_digits=14,decimal_places=2)
    currency=models.CharField(max_length=3,default="INR")
    status=models.CharField(max_length=30,default="RECEIVED")
    created_at=models.DateTimeField(auto_now_add=True)

class Incident(models.Model):
    SEVERITY=[("LOW","LOW"),("MEDIUM","MEDIUM"),("HIGH","HIGH"),("CRITICAL","CRITICAL")]
    STATUS=[("OPEN","OPEN"),("IN_PROGRESS","IN_PROGRESS"),("RESOLVED","RESOLVED"),("CLOSED","CLOSED")]
    title=models.CharField(max_length=250)
    severity=models.CharField(max_length=20,choices=SEVERITY)
    status=models.CharField(max_length=30,choices=STATUS,default="OPEN")
    customer=models.CharField(max_length=160)
    owner=models.CharField(max_length=160)
    sla_hours=models.PositiveIntegerField(default=8)
    rca=models.TextField(blank=True)
    resolution=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    resolved_at=models.DateTimeField(null=True,blank=True)

class AuditLog(models.Model):
    actor=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    action=models.CharField(max_length=80)
    entity=models.CharField(max_length=80)
    entity_id=models.IntegerField(null=True,blank=True)
    details=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
