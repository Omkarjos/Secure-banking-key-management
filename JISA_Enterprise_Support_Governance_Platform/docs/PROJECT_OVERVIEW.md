# Project Overview

## Business scenario
A simulated enterprise banking customer uses a security/application platform. The engineering team needs to manage incidents, SLA, implementation work, customer commitments and operational governance.

## Role mapping

### Implementation & Support Engineer
- Installation/configuration lifecycle
- Health checks
- Incident ownership
- SLA tracking
- RCA
- Production reporting
- Change and maintenance awareness

### Program & Operations Coordinator
- Project/workstream tracking
- Action and dependency tracking
- Risk visibility
- Executive reporting
- Governance cadence
- Customer commitment tracking

## Architecture

Browser → Nginx → Flask REST application → SQLite demo database.

The application is Dockerized so the architecture can later be switched to PostgreSQL.
