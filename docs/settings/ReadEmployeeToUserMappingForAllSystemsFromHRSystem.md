# Read Employee To User Mapping For All Systems From HR System

**Technical Name:** ReadEmployeeToUserMappingForAllSystemsFromHRSystem

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the system reads and applies employee to user mapping rules for all systems from the HR system. When enabled, the system will use custom mapping rules to determine the correct employee ID for users based on the data from the HR system.

**Business Impact:**

Enabling this setting ensures that user accounts across all systems are correctly associated with the right employee entities from the HR system, enhancing data integrity and consistency across the organization. It is particularly beneficial in complex environments with multiple user accounts per employee across different systems.

**Technical Impact when configured:**

When configured, this parameter activates the process of applying pre-defined employee to user mapping rules. These rules are used to determine and associate the correct employee ID to user accounts across systems, based on the information provided by the HR system. This association is crucial for maintaining accurate and consistent user identification and for supporting various HR and security processes.

**Examples Scenario:**

- **Before enabling:** Employee IDs may mismatch or not be consistently mapped across systems, leading to potential security risks or issues in auditing and reporting.
- **After enabling:** The system enforces a consistent mapping of employee IDs to user accounts across all systems, ensuring accurate tracking and management of user access and activities.

**Related Settings:**

- ShowSodSeverityDescription

**Best Practices:** configure when, avoid when 

- **Configure when:**
  - You have a complex IT environment with users having multiple accounts across various systems.
  - Accurate employee to user mapping is critical for your security, compliance, and operational needs.
- **Avoid when:**
  - Your organization does not have a structured or consistent HR system in place to provide reliable employee data.
  - Your organization operates on a highly simplistic IT infrastructure with minimal user accounts, making complex mappings unnecessary.