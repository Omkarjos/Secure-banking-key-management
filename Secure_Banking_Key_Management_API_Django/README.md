# Secure Banking Key Management & API Platform

A GitHub-ready portfolio project aligned with the JISA Implementation & Support Engineer role.

## What it demonstrates
- Django + Django REST Framework
- PostgreSQL
- JWT authentication
- REST APIs and Postman
- Key lifecycle: generation, rotation, revocation
- Certificate lifecycle and expiry tracking
- Banking transaction demo API
- Audit logging
- Incident and SLA management
- Health monitoring
- Docker / Docker Compose
- Nginx reverse proxy
- SSL/TLS
- Linux deployment and support scripts
- Runbook, SOP, RCA and change-management documentation

> Security note: this is a learning/portfolio simulation, not a real HSM/KMS or banking production system. A real deployment would use an approved HSM/KMS and enterprise PKI.

## Start with Docker

```bash
docker compose up --build
```

Open `http://localhost:8080`

Admin:
`http://localhost:8080/admin/`

Demo API user:
`admin@example.com` / `Admin@123`

## API
- POST `/api/auth/token/`
- POST `/api/auth/token/refresh/`
- GET `/api/health/`
- GET/POST `/api/keys/`
- POST `/api/keys/{id}/rotate/`
- POST `/api/keys/{id}/revoke/`
- GET/POST `/api/certificates/`
- GET/POST `/api/incidents/`
- POST `/api/incidents/{id}/resolve/`
- GET/POST `/api/transactions/`
- GET `/api/audit/`

## Local non-Docker setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=sqlite:///db.sqlite3
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

## Project mapping to JISA JD

| JD requirement | Project evidence |
|---|---|
| Linux administration | `ops/health_check.sh`, `ops/deploy.sh` |
| TCP/IP / reverse proxy | Nginx configuration |
| SSL/TLS | `scripts/generate_certs.sh` |
| HSM/PKI concepts | Key and certificate lifecycle modules |
| REST APIs / Postman | DRF API + collection |
| PostgreSQL | Docker PostgreSQL + Django ORM |
| Application implementation | Docker/Django/Nginx deployment |
| Monitoring | Health endpoint + operational script |
| Incident/SLA | Incident model + SLA fields |
| RCA | `docs/RCA_TEMPLATE.md` |
| Change management | `docs/CHANGE_RECORD.md` |
| Runbooks/SOPs | `docs/RUNBOOK.md`, `docs/SOP_DEPLOYMENT.md` |
| Audit trail | AuditLog model/API |
