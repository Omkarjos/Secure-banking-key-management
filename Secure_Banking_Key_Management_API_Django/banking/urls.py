from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import KeyViewSet,CertificateViewSet,TransactionViewSet,IncidentViewSet,AuditViewSet,health
router=DefaultRouter()
router.register("keys",KeyViewSet,basename="key")
router.register("certificates",CertificateViewSet)
router.register("transactions",TransactionViewSet)
router.register("incidents",IncidentViewSet)
router.register("audit",AuditViewSet)
urlpatterns=[path("health/",health),path("",include(router.urls))]
