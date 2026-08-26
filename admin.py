from django.contrib import admin
from .models import Key,Certificate,Transaction,Incident,AuditLog
for model in [Key,Certificate,Transaction,Incident,AuditLog]:
    admin.site.register(model)
