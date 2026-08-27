# Application Deployment SOP

## Pre-check
- Confirm approved deployment window.
- Back up configuration/database.
- Check disk and memory.
- Confirm dependencies.
- Confirm rollback package.

## Deployment
- Build Docker image.
- Start container.
- Verify `/api/health`.
- Validate API and dashboard.
- Review logs.

## Post-check
- Execute smoke tests.
- Confirm no critical errors.
- Update change record.
- Communicate completion.

## Rollback
- Stop failed version.
- Restore previous image/configuration.
- Verify health endpoint.
- Document incident/change outcome.
