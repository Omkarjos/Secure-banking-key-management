from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from banking.models import Key,Certificate,Incident
from banking.services import generate_key

class Command(BaseCommand):
    help="Create demonstration data"
    def handle(self,*args,**kwargs):
        user,created=User.objects.get_or_create(username="admin",defaults={"email":"admin@example.com","is_staff":True,"is_superuser":True})
        if created: user.set_password("Admin@123"); user.save()
        if not Key.objects.exists(): generate_key("payment-api-master")
        if not Certificate.objects.exists():
            Certificate.objects.create(common_name="api.bank.local",serial_number="DEMO-001",
              expires_at=timezone.now()+timedelta(days=60))
        if not Incident.objects.exists():
            Incident.objects.create(title="Payment API latency",severity="HIGH",
              customer="Demo PSU Bank",owner="Support Engineer",sla_hours=4)
        self.stdout.write(self.style.SUCCESS("Demo data ready."))
