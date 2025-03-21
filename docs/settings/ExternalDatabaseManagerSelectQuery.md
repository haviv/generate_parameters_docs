# External Database Manager Select Query

**Technical Name:** ExternalDatabaseManagerSelectQuery

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The External Database Manager Select Query parameter is utilized to define the specific SQL query that should be executed to retrieve organizational structure data from an external database. This setting supports the integration with external databases by specifying how the Pathlock Cloud GRC platform should request data to align with the deployed organizational structure.

**Business Impact:**

Correct configuration of this parameter ensures that the organizational structure within the Pathlock Cloud GRC platform accurately reflects the structure stored within an external database. This is critical for ensuring that security, risk, and compliance data are mapped correctly to the organization's structure.

**Technical Impact when configured:**

- When configured correctly, enables the seamless integration of the Pathlock Cloud GRC platform with external databases, ensuring that organizational structure data is accurately imported and represented.
- Misconfiguration could lead to incorrect organizational data representation, affecting the application of GRC controls and policies.

**Examples Scenario:**

If an organization uses a custom database schema to manage their departments and user roles, the External Database Manager Select Query can be configured to extract this specific information in a format compatible with the Pathlock Cloud GRC platform. For example, a SQL query like `SELECT department_id, department_name, user_role FROM custom_org_structure_table` could be set as the value for this parameter.

**Related Settings:** 

- MitigateViolation_ShowApproveReasonOnly

**Best Practices:** configure when integrating Pathlock Cloud GRC with external databases to align organizational structures. Avoid when the organizational data does not require synchronization with external databases, or when the database schema does not support the required query structure.