# Active Employees HR Query

**Technical Name:** ActiveEmployeesHRQuery

**Category:** HR

**Default Value:**

**Impact Level:** High

**Description:**

The Active Employees HR Query parameter is designed to aid in the retrieval and management of active employee data from HR systems. This is critical for ensuring that only current employees have access to specific resources and to maintain the accuracy of organizational structure information.

**Business Impact:**

Improper configuration can lead to unauthorized access or the exclusion of valid employees from accessing necessary resources, affecting operational efficiency and security compliance.

**Technical Impact when configured:**

Correct configuration ensures real-time synchronization of employee status, updates organizational roles and access permissions, and maintains compliance with security policies by ensuring only active employees have access privileges.

**Examples Scenario:**

A new policy requires that only active employees should have access to a confidential financial reporting tool. By configuring the ActiveEmployeesHRQuery parameter correctly, the organization ensures that as soon as an employee's status changes to inactive (e.g., resignation, termination), their access to the tool is automatically revoked.

**Related Settings:**

- ActiveDirectoryEmployeeIdMinimumLength

**Best Practices:** 

- Configure the Active Employees HR Query to run at regular intervals to ensure that the organization's access controls are always in sync with the current employee roster. 
- Avoid manual adjustments and rely on automated synchronization to reduce the risk of security breaches and compliance issues.