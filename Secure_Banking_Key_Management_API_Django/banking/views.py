from datetime import timedelta
from django.db import connection
from django.utils import timezone
from rest_framework import viewsets,status
from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Key,Certificate,Transaction,Incident,AuditLog
from .serializers import KeySerializer,CertificateSerializer,TransactionSerializer,IncidentSerializer,AuditSerializer
from .services import generate_key,rotate_key,revoke_key

def audit(user,action,entity,obj,details=""):
    AuditLog.objects.create(actor=user,action=action,entity=entity,entity_id=obj.id,details=details)

class KeyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Key.objects.all().order_by("-id")
    serializer_class=KeySerializer
    @action(detail=False,methods=["post"])
    def create_key(self,request):
        alias=request.data.get("alias")
        if not alias: return Response({"error":"alias is required"},400)
        key=generate_key(alias); audit(request.user,"CREATE","Key",key,alias)
        return Response(KeySerializer(key).data,status=201)
    @action(detail=True,methods=["post"])
    def rotate(self,request,pk=None):
        key=rotate_key(self.get_object()); audit(request.user,"ROTATE","Key",key,f"version={key.version}")
        return Response(KeySerializer(key).data)
    @action(detail=True,methods=["post"])
    def revoke(self,request,pk=None):
        key=revoke_key(self.get_object()); audit(request.user,"REVOKE","Key",key,key.alias)
        return Response(KeySerializer(key).data)

class CertificateViewSet(viewsets.ModelViewSet):
    queryset=Certificate.objects.all().order_by("-id")
    serializer_class=CertificateSerializer
    def perform_create(self,serializer):
        c=serializer.save()
        audit(self.request.user,"CREATE","Certificate",c,c.common_name)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all().order_by("-id")
    serializer_class=TransactionSerializer
    def perform_create(self,serializer):
        t=serializer.save()
        audit(self.request.user,"CREATE","Transaction",t,t.reference)

class IncidentViewSet(viewsets.ModelViewSet):
    queryset=Incident.objects.all().order_by("-id")
    serializer_class=IncidentSerializer
    def perform_create(self,serializer):
        i=serializer.save()
        audit(self.request.user,"CREATE","Incident",i,i.title)
    @action(detail=True,methods=["post"])
    def resolve(self,request,pk=None):
        i=self.get_object()
        i.status="RESOLVED"; i.resolution=request.data.get("resolution",""); i.resolved_at=timezone.now()
        i.save(); audit(request.user,"RESOLVE","Incident",i,i.resolution)
        return Response(IncidentSerializer(i).data)

class AuditViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=AuditLog.objects.all().order_by("-id")
    serializer_class=AuditSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    try:
        with connection.cursor() as cursor: cursor.execute("SELECT 1")
        db="UP"
    except Exception: db="DOWN"
    return Response({"service":"secure-banking-api","status":"UP" if db=="UP" else "DEGRADED","database":db})
