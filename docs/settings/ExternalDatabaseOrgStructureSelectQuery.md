# External Database Org Structure Select Query

**Technical Name:** ExternalDatabaseOrgStructureSelectQuery

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

The External Database Org Structure Select Query parameter configures the SQL select query used to retrieve organizational structure data from an external database. This configuration is crucial for organizations utilizing an external database to manage their hierarchy and requiring synchronization with the Pathlock Cloud GRC platform for accurate risk, compliance, and security management.

**Business Impact:**

Configuring this parameter correctly ensures that the Pathlock platform accurately reflects the organization's structure, which is essential for implementing security controls, audit trails, risk assessment, and compliance reporting based on the organizational hierarchy. Misconfiguration can lead to inaccurate risk assessments, compliance issues, and ineffective security measures.

**Technical Impact when configured:**

When properly configured, the parameter enables the Pathlock platform to connect to an external database and execute the defined SQL select query to import the organizational structure data. This allows for dynamic updating of the organizational structure in the Pathlock platform, reflecting any changes made in the external database.

**Examples Scenario:**

An organization wishes to integrate Pathlock Cloud GRC with its external Human Resources Management System (HRMS), where all employee roles and departmental structures are stored. By configuring the ExternalDatabaseOrgStructureSelectQuery parameter with a SQL query tailored to fetch the organizational hierarchy from the HRMS database, the organization can automate the process of reflecting these structures within Pathlock, ensuring accurate and up-to-date data for GRC processes.

**Related Settings:** 

- ScheduleAuthorizationReviewUseRecurrenceParameter

**Best Practices:** 

- **Configure when:** There's a need to align Pathlock Cloud GRC's internal data representation with an external source of truth for organizational structure.
  
- **Avoid when:** The organization's structure is static, simple, or already manually managed within Pathlock with minimal changes over time. In such cases, the overhead of maintaining an external synchronization may not justify the benefits.