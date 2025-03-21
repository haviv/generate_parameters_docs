# External Database Employees Select Query

**Technical Name:** ExternalDatabaseEmployeesSelectQuery

**Category:** Configuration

**Default Value:** *Not provided in the given context.*

**Impact Level:** High

**Description:**

This parameter is utilized for specifying the SQL query to select employee data from an external database. It is integral to the process of importing or synchronizing employee records into the Pathlock Cloud GRC platform from external sources.

**Business Impact:**

Correct configuration of this parameter ensures that the employee data imported into the Pathlock system is current and accurate. This is crucial for maintaining up-to-date access rights, compliance, and security across the organization's systems and applications.

**Technical Impact when configured:**

When correctly configured, this parameter allows for seamless integration with external databases, ensuring that employee information is accurately reflected in the Pathlock platform. Misconfiguration can lead to incomplete or incorrect data synchronization, potentially compromising compliance and security policies.

**Examples Scenario:**

- An organization might use the following SQL query to import employee details from an external HR database: `SELECT employeeId, firstName, lastName FROM Employees WHERE status = 'active'`. In this scenario, only active employees are imported into the Pathlock Cloud GRC platform, ensuring that the system reflects the current workforce.
  
**Related Settings:**

- `ExternalDatabaseProvider.RemoveEmployeesByStatus(result)` - This setting is related as it suggests a function to remove employees based on their status after performing the select query operation, ensuring the Pathlock platform contains up-to-date employee status information.

**Best Practices:** 

- **Configure when:** There's a need to import or sync employee data from an external database into the Pathlock platform for accurate access rights and compliance management.
- **Avoid when:** The external database structure or data fields do not align with the organization's employee information requirements in Pathlock.