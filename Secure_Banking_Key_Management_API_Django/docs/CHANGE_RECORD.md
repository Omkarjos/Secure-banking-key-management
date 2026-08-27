# Sample Change Record

Change: Deploy Secure Banking API v1.0
Environment: Portfolio production-like environment
Risk: Medium

Pre-check:
- Database backup: PASS
- Health baseline: PASS
- Rollback plan: PASS

Implementation:
- Build Docker image
- Start PostgreSQL
- Run migrations
- Seed demo data
- Start Django/Gunicorn
- Start Nginx

Validation:
- Health API: PASS
- Authentication: PASS
- Key lifecycle: PASS
- Incident API: PASS

This is a portfolio simulation and does not represent approval for a real bank.
