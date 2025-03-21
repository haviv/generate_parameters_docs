# Sql Error For PKViolation Retries

**Technical Name:** SqlErrorForPKViolationRetries

**Category:** Configuration

**Default Value:** 2627

**Impact Level:** Medium

**Description:** This parameter specifies the SQL error code used by the system to identify primary key violation errors. This error occurs when an attempt is made to insert a record with a primary key that already exists in the database.

**Business Impact:** Properly configuring this parameter ensures that the system accurately identifies and handles primary key violation errors, which is critical for maintaining data integrity and avoiding potential data loss or corruption. It enables the system to rerun transactions that failed due to primary key conflicts, thus improving overall system reliability and reducing manual intervention needs.

**Technical Impact when configured:** When set, this parameter allows the system to automatically retry operations that fail due to a primary key violation error, based on the specified SQL error code. This can reduce the need for manual error handling and can help in maintaining the consistency and integrity of data within the database.

**Example Scenario:** Consider an automated data import process that attempts to insert multiple records into a database. If two records in the import batch unintentionally have the same primary key value, a primary key violation error will occur. With the correct `SqlErrorForPKViolationRetries` value configured, the system can recognize this specific error type and apply predefined logic to handle the error, such as skipping the conflicting record or generating a unique key and retrying the insertion, thereby preventing the import process from failing.

**Related Settings:** Not Applicable

**Applicable Workflows Actions:** Not Applicable

**Best Practices:** Configure this parameter at the initial setup of the Pathlock GRC platform to match the SQL error code for primary key violation errors in your database management system (the default is set for SQL Server). Avoid changing this setting without validating the error code for primary key violations in the current version of your database management system to prevent misidentification of errors and potential data handling issues.