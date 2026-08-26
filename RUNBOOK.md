# Production Support Runbook

## Health
```bash
./ops/health_check.sh
docker compose ps
./ops/logs.sh
```

## Incident workflow
1. Confirm impact and scope.
2. Check API health.
3. Check application logs.
4. Check PostgreSQL.
5. Review recent changes.
6. Mitigate and restore service.
7. Record evidence.
8. Perform RCA.
9. Implement permanent corrective action.
10. Close incident after validation.

## Key lifecycle
Create → Activate → Rotate → Revoke → Audit.

## Certificate lifecycle
Register → Monitor expiry → Renew → Revoke/retire.

A real banking environment should keep cryptographic key material inside approved HSM/KMS controls.
