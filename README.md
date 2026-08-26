# 🔐 Secure Banking Key Management & API Platform

A production-style backend project that simulates a secure banking
key-management and API platform using Django, Django REST Framework,
PostgreSQL, Docker, Nginx and SSL/TLS.

The project focuses on secure API development, cryptographic key lifecycle
management, certificate tracking, production support, incident management,
SLA monitoring and audit logging.

> ⚠️ **Security Disclaimer**
>
> This is a portfolio/learning project. It is NOT a real banking system,
> HSM or production KMS. Real banking environments should use approved
> HSM/KMS infrastructure, enterprise PKI, secrets management and appropriate
> regulatory/security controls.

---

## 🚀 Project Overview

The platform simulates the backend services that could support an enterprise
banking/security environment.

It provides APIs for:

- 🔑 Cryptographic key lifecycle management
- 🔄 Key rotation
- 🚫 Key revocation
- 🔐 JWT authentication
- 📜 Certificate management
- 🏦 Banking transaction records
- 🚨 Incident management
- ⏱️ SLA tracking
- 📝 Audit logging
- ❤️ Application health monitoring
- 🐳 Docker-based deployment
- 🌐 Nginx reverse proxy
- 🐧 Linux operational scripts
- 🔒 SSL/TLS certificate generation
- 📚 Production support documentation

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django REST Framework | REST API development |
| PostgreSQL | Production database |
| SQLite | Local development option |
| JWT | API authentication |
| Cryptography / Fernet | Demonstration key material protection |
| Docker | Containerization |
| Docker Compose | Multi-container deployment |
| Nginx | Reverse proxy |
| Gunicorn | Django application server |
| Linux Bash | Deployment and monitoring scripts |
| OpenSSL | Demo SSL/TLS certificate generation |
| Postman | API testing |
| Swagger/OpenAPI | API documentation |

---

# 🏗️ System Architecture

```text
                 Banking / Client Application
                           |
                           | HTTPS
                           ↓
                  ┌─────────────────┐
                  │      NGINX      │
                  │ Reverse Proxy   │
                  └────────┬────────┘
                           |
                           ↓
                ┌──────────────────────┐
                │ Django REST Framework│
                │      + Gunicorn      │
                └──────────┬───────────┘
                           |
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
 Authentication      Key Management     Certificate
    & JWT              Service           Management
        │                  │                  │
        └──────────────────┼──────────────────┘
                           |
                           ↓
                    ┌─────────────┐
                    │ PostgreSQL  │
                    └──────┬──────┘
                           |
                           ↓
                     Audit Logs
