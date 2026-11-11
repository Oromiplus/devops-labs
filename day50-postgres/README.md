# Day 51 — PostgreSQL Reliability and Configuration Hardening

## Objectives
- Externalise database credentials into an environment file.
- Keep credentials out of version control.
- Add a PostgreSQL health check.
- Configure automatic container restart behaviour.
- Verify database connectivity and persistent storage.

## Configuration
- Image: postgres:17
- Compose service: database
- Container: postgres-db
- Database: devopsdb
- Host port: 5432
- Persistent storage: postgres-data
- Restart policy: unless-stopped

## Security
Database environment variables are supplied through a local `.env` file.
The environment file is excluded from Git and must not be committed.
The Compose configuration references variables rather than hardcoding
credential values.

## Health and Reliability Verification
- Compose configuration validation succeeded.
- PostgreSQL health check reported healthy.
- PostgreSQL accepted connections using pg_isready.
- Docker Compose listed the database as running and healthy.
- The existing deployments table retained all three records after
  the container was restarted.
- The named PostgreSQL volume was preserved.

## Deployment Records Verified
- project-exodus-api
- frontend
- postgres-db

## Lessons Learned
- A container can exit normally without an application error.
- A restart policy helps recover from unexpected container stops.
- Named volumes preserve database data beyond a container's lifecycle.
- Health checks help distinguish a running container from a ready service.
- Credentials should be externalised and excluded from version control.

## Limitations
This is a development lab configuration, not a complete production
security or disaster-recovery setup. Production deployments also need
appropriate secret management, backups, restore testing, access controls,
and monitoring.
