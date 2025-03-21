# Show Employee Change Data

**Technical Name:** ShowEmployeeChangeData

**Category:** Audit

**Default Value:** N/A

**Impact Level:** High

**Description:**

Enables the visibility of data pertaining to changes in employee records within the system, providing administrators and audit personnel with detailed insights into updates, insertions, and deletions of employee-related information. 

**Business Impact:**

Improves governance by allowing for thorough monitoring and reviewing of alterations in employee details, which is critical for maintaining up-to-date and accurate employee records. Enhances security by enabling the tracking of unauthorized or erroneous changes, thus aiding in compliance with various regulations.

**Technical Impact when configured:**

- `PT_UPDATE_U`: Represents an update made to an existing employee's record.
- `PT_UPDATE_I`: Indicates the insertion of a new employee's record.
- `PT_UPDATE_D`: Signifies the deletion of an employee's record.

These identifiers aid in the categorization and audit of employee data modifications, supporting compliance and security measures.

**Examples Scenario:**

A company's HR department regularly updates employee information in the Pathlock Cloud GRC system following promotions, role changes, or terminations. Configuring the ShowEmployeeChangeData parameter allows the security team to audit these changes efficiently, ensuring that all updates are authorized and accurately recorded, thus maintaining the integrity of the employee data within the organization.

**Related Settings:**

N/A

**Best Practices:** 

- **Configure when:** You need to audit changes to employee data regularly or comply with regulatory requirements that mandate strict oversight of employee record modifications.
- **Avoid when:** There is no requirement for auditing employee changes, or such visibility might infringe on privacy regulations without proper authorization or safeguards in place.