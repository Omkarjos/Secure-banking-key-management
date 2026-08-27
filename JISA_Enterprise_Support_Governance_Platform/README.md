# JISA Enterprise Support & Governance Platform

A portfolio project designed around the two JISA roles:
1. Implementation & Support Engineer
2. Program & Operations Coordinator

## What this project demonstrates

### Technical / Implementation
- REST API
- PostgreSQL-ready database
- Authentication-ready architecture
- Incident and SLA management
- Application health monitoring
- Audit logging
- Root Cause Analysis (RCA)
- Linux/Docker deployment
- Nginx reverse proxy configuration
- Operational runbooks and SOPs

### Program / Operations
- Project and workstream tracking
- Milestones
- RAID log
- RACI matrix
- Decision log
- Action tracker
- Customer commitments
- Weekly status reporting
- Management dashboard

## Tech Stack
- Python 3.11
- Flask
- SQLite for zero-setup local demo
- PostgreSQL configuration for production
- HTML/CSS/JavaScript
- Docker / Docker Compose
- Nginx
- REST APIs

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Run with Docker

```bash
docker compose up --build
```

Open http://localhost:5000

## Main API endpoints

- GET /api/health
- GET /api/incidents
- POST /api/incidents
- GET /api/projects
- GET /api/metrics
- GET /api/activities

## Portfolio talking points

This is a simulated enterprise banking-support environment. It does not implement a real HSM or cryptographic key-management appliance. The project demonstrates the surrounding implementation/support workflow: deployment, monitoring, incidents, SLA, RCA, governance, documentation and reporting.
