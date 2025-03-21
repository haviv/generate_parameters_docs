# Employee Natural Key Column

**Technical Name:** EmployeeNaturalKeyColumn

**Category:** User Management

**Default Value:** None

**Impact Level:** High

**Description:**

The Employee Natural Key Column parameter is designed to identify and differentiate employees within the organization uniquely. It serves as a critical element in syncing and mapping organizational data, ensuring that each employee's record is accurately maintained.

**Business Impact:**

Configuring the Employee Natural Key Column correctly impacts the integrity of employee data, positively affecting operations such as access reviews, authorization processes, and overall security posture management. It ensures that employees are correctly identified, preventing potential security risks arising from misidentification.

**Technical Impact when configured:**

Upon configuration, the Employee Natural Key Column ensures that employee data is synchronized correctly across different systems. It aids in the effective mapping of direct manager relationships and the accurate application of rules and policies at an individual level.

**Examples Scenario:**

- **Scenario:** An organization wishes to automate the process of updating employee role changes in its GRC platform. By configuring the Employee Natural Key Column, the system can accurately identify each employee and update their information accordingly, ensuring that access rights and responsibilities reflect their current role.

**Related Settings:** 

- `employeeAlternativeKeyColumn` - This setting might be used in tandem with Employee Natural Key Column to provide alternative identification methods for employees.

**Best Practices:** 

- **Configure when**: You have a definitive and consistent unique identifier for each employee across your organization's systems.
- **Avoid when**: Your organization does not have a unique attribute that consistently identifies each employee across different systems, as this could lead to misidentification and potential security risks.