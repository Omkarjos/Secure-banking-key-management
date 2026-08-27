# Production Support Runbook

## 1. Health Check
1. Open `/api/health`.
2. Confirm status is `UP`.
3. Check application logs.
4. Check database availability.

## 2. Incident Handling
1. Record incident.
2. Assign severity and owner.
3. Confirm SLA target.
4. Investigate logs and recent changes.
5. Restore service.
6. Document RCA.
7. Add permanent corrective action.
8. Close only after validation.

## 3. Escalation
- L1: Basic health, configuration and known issue checks.
- L2: Application, integration and database troubleshooting.
- L3: Product engineering escalation with logs, timestamps, impact and reproduction details.

## 4. Change Management
All production changes should have an approved change window, rollback plan, validation steps and post-change verification.
