from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
urlpatterns=[
 path("admin/",admin.site.urls),
 path("api/auth/token/",TokenObtainPairView.as_view()),
 path("api/auth/token/refresh/",TokenRefreshView.as_view()),
 path("api/",include("banking.urls")),
 path("api/schema/",SpectacularAPIView.as_view()),
 path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema")),
]
