**External Database Employee Status To Exclude**

**Technical Name:** ExternalDatabaseEmployeeStatusToExclude

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter is utilized to exclude specific employee statuses from being imported into the Pathlock platform from an external database. It is particularly useful in managing which employees are considered active or inactive within the GRC platform, based on their employment status in external HR or organizational management systems.

**Business Impact:**

By configuring this parameter, organizations can ensure that only employees with relevant statuses are included in the Pathlock platform, which is crucial for accurate access control, compliance reporting, and risk management. It helps in maintaining streamlined operations and preventing unauthorized access by excluding employees who are not currently active, such as those on leave, retired, or terminated.

**Technical Impact when configured:**

When this parameter is configured, the Pathlock platform will omit employees with the specified statuses during the synchronization process with external databases. This results in a cleaner, more accurate representation of the currently active workforce, enhancing security and compliance measures by only including employee data that is relevant for ongoing operations and auditing purposes.

**Example Scenario:**

For instance, an organization might use this parameter to exclude employees with statuses like "Retired", "On Leave", or "Terminated". This ensures that access rights and compliance reports generated within the Pathlock platform accurately reflect the current, active workforce, excluding those who should not have access to company resources or be part of compliance and risk assessments.

**Related Settings:** 

- No directly related settings found in the provided code references.

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** You need to keep the employee data in Pathlock synchronized with current active employees by excluding those with specific statuses from external systems. This is especially important for large organizations looking to automate access control and compliance processes efficiently.
  
- **Avoid when:** All employees in the external database should be imported into Pathlock regardless of their status. This could be relevant for smaller organizations or specific use cases where status does not impact access control, compliance, and risk management processes.