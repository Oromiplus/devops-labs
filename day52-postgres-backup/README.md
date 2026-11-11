# Day 52 — PostgreSQL Backup and Recovery

## Objectives
- Create a PostgreSQL logical backup using pg_dump.
- Store backups outside the database container.
- Inspect and verify backup contents.
- Restore a database into a separate test database.
- Verify restored records against the original.
- Secure backup file permissions.

## Environment
- PostgreSQL image: postgres:17
- Container: postgres-db
- Original database: devopsdb
- Test database: devopsdb_restore_test
- Database user: admin
- Backup format: SQL
- Backup location: ~/devops-labs/backups/devopsdb_day52.sql

## Backup Procedure
Created a logical database backup using pg_dump.

The backup was stored on the Ubuntu host rather than
inside the PostgreSQL container.

## Backup Verification
- Backup file successfully created.
- SQL dump completion marker verified.
- Deployments table definition verified.
- Three deployment records found in the backup.

## Recovery Procedure
- Created a separate restoration database.
- Restored the SQL backup using psql.
- Confirmed successful table creation and data import.

## Recovery Verification
The restored database contained all three records:

1. project-exodus-api
2. frontend
3. postgres-db

All record IDs, statuses, environments and timestamps
matched the original database.

The original devopsdb was also checked and retained
all three records.

## Security
Backup file permissions changed from 644 to 600.

Only the file owner has read and write permissions.

The actual SQL backup is kept outside the Git repository
and must not be committed.

## Lessons Learned
- pg_dump creates logical PostgreSQL backups.
- psql can restore SQL-format backups.
- Backups should be stored outside database containers.
- Restoration must be tested, not merely assumed.
- File permissions protect sensitive backup contents.
- A separate test database allows recovery testing
  without risking production or original data.

## Limitations
This exercise demonstrates logical backup and recovery.
Production environments also require automated backup
scheduling, off-site storage, retention policies,
encryption and periodic restore testing.
