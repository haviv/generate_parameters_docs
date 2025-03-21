# Filter Out Terminated Employees From Employees Data

**Technical Name:** FilterOutTerminatedEmployeesFromEmployeesData

**Category:** User Management

**Default Value:** True

**Impact Level:** High

**Description:**

This parameter controls whether terminated employees are filtered out from the employees data during synchronization processes. 

**Business Impact:**

Maintaining a current and accurate list of active employees is crucial for operations, security, and compliance. Including terminated employees can lead to incorrect access rights, reporting errors, and potential security vulnerabilities.

**Technical Impact when configured:**

When enabled, the system will exclude any terminated employees from data sync operations, ensuring that only current employees are considered in user access and permissions assignments. This helps in maintaining the integrity of the security model and compliance posture.

**Examples Scenario:**

1. During a routine audit, a company must demonstrate that only current employees have access to sensitive systems. By enabling this parameter, the company can efficiently ensure compliance with internal policies and regulatory requirements.
2. A business is undergoing a system upgrade and needs to migrate user data. Filtering out terminated employees simplifies the migration process and minimizes the risk of migrating outdated information.

**Related Settings:**

- `OverrideRoleEndDateToSAP`

**Best Practices:** configure when the business requires strict adherence to current employee data for security and compliance purposes; avoid when comprehensive historical data analysis, including terminated employees, is needed.