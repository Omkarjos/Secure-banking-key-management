import os
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.getenv("SECRET_KEY","dev-secret")
DEBUG=os.getenv("DEBUG","1")=="1"
ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS","localhost,127.0.0.1").split(",")

DATABASE_URL=os.getenv("DATABASE_URL","sqlite:///"+str(BASE_DIR/"db.sqlite3"))
if DATABASE_URL.startswith("postgresql"):
    p=urlparse(DATABASE_URL)
    DATABASES={"default":{
        "ENGINE":"django.db.backends.postgresql",
        "NAME":p.path.lstrip("/"),"USER":p.username,"PASSWORD":p.password,
        "HOST":p.hostname,"PORT":p.port or 5432
    }}
else:
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}

INSTALLED_APPS=[
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
    "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "rest_framework","drf_spectacular","banking"
]
MIDDLEWARE=[
    "django.middleware.security.SecurityMiddleware","django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware"
]
ROOT_URLCONF="config.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR/"templates"],
"APP_DIRS":True,"OPTIONS":{"context_processors":[
"django.template.context_processors.request","django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION="config.wsgi.application"
STATIC_URL="/static/"
STATIC_ROOT=BASE_DIR/"staticfiles"
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
REST_FRAMEWORK={
 "DEFAULT_AUTHENTICATION_CLASSES":("rest_framework_simplejwt.authentication.JWTAuthentication",),
 "DEFAULT_PERMISSION_CLASSES":("rest_framework.permissions.IsAuthenticated",),
 "DEFAULT_SCHEMA_CLASS":"drf_spectacular.openapi.AutoSchema"
}
SPECTACULAR_SETTINGS={"TITLE":"Secure Banking Key Management API","VERSION":"1.0.0"}
