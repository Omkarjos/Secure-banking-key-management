# Deployment SOP

## Pre-change
- Approved change ticket
- Maintenance window
- Database backup
- Rollback plan
- Stakeholder notification

## Deployment
```bash
./ops/deploy.sh
```

## Validation
- `/api/health/`
- JWT login
- Key list
- Certificate list
- Incident API
- PostgreSQL connectivity
- Nginx proxy

## Rollback
Stop the release and restore the previously approved image/configuration.

## Post-change
- Record result
- Update change ticket
- Monitor during hypercare
- Send completion update
