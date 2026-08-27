from rest_framework import serializers
from .models import Key,Certificate,Transaction,Incident,AuditLog

class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model=Key
        fields=["id","alias","algorithm","version","status","created_at","rotated_at"]

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields="__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields="__all__"
        read_only_fields=["created_at"]

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incident
        fields="__all__"
        read_only_fields=["created_at","resolved_at"]

class AuditSerializer(serializers.ModelSerializer):
    actor=serializers.StringRelatedField()
    class Meta:
        model=AuditLog
        fields="__all__"
