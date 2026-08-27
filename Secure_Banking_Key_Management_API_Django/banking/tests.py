from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class HealthTest(TestCase):
    def test_health(self):
        response=APIClient().get("/api/health/")
        self.assertEqual(response.status_code,200)

class AuthTest(TestCase):
    def test_token(self):
        u=User.objects.create_user(username="tester",password="Test@123")
        r=APIClient().post("/api/auth/token/",{"username":"tester","password":"Test@123"},format="json")
        self.assertEqual(r.status_code,200)
