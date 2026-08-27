# API Examples

## Health
GET `/api/health`

## Incidents
GET `/api/incidents`

POST `/api/incidents`

Example JSON:
```json
{
  "title": "Payment API unavailable",
  "severity": "High",
  "owner": "Support Team",
  "customer": "PSU Bank",
  "sla_hours": 4
}
```

## Metrics
GET `/api/metrics`

## Projects
GET `/api/projects`
