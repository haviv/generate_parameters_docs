# Sql Error For PKViolation

**Technical Name:** SqlErrorForPKViolation

**Category:** Configuration

**Default Value:** 2601

**Impact Level:** Medium

**Description:**

This setting configures the specific SQL error code that the Pathlock Cloud GRC platform identifies and handles as a primary key violation error. This is particularly useful for managing database integrity and preventing duplicate records.

**Business Impact:**

Improper configuration of this parameter can lead to unhandled errors during data synchronization or updates, potentially causing data corruption or loss. Correctly setting this parameter ensures that the platform can appropriately handle duplicate key exceptions, maintaining data integrity and operational continuity.

**Technical Impact when configured:**

When properly configured, the Pathlock Cloud GRC platform will correctly identify and handle SQL errors related to primary key violations, preventing the addition of duplicate records in the database and ensuring that workflows requiring unique identifiers for operations function correctly.

**Examples Scenario:**

Suppose an administrator tries to insert a new user record into the Pathlock Cloud GRC platform's database, but the user's unique identifier already exists. With `SqlErrorForPKViolation` correctly set, the platform identifies this operation as a primary key violation and can execute programmed error handling procedures, such as alerting the administrator or aborting the operation, to prevent duplicate records.

**Related Settings:** N/A

**Best Practices:** Configure this parameter to match the SQL database's specific error code for a duplicate primary key violation. Avoid arbitrary changes to this setting without understanding the database's error codes and the potential impact on data integrity.