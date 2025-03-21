# Check SoD For Employees With Multi System Access

**Technical Name:** CheckSodForEmployeesWithMultiSystemAccess

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter is designed to automate the process of checking Segregation of Duties (SoD) conflicts across multiple systems for all employees. It ensures that no single employee has access rights that can lead to potential conflicts of interest or compromise the integrity of the systems. This checking process is crucial for maintaining the security and compliance of the IT infrastructure in organizations that use the Pathlock Cloud GRC platform.

**Business Impact:**

Improper segregation of duties can result in fraud, error, and inefficiency, leading to significant financial losses and damage to the organization's reputation. By automating SoD checks, organizations can swiftly identify and remediate access-related risks, thereby enhancing their control environment and compliance posture.

**Technical Impact when configured:**

When enabled, this function iterates through all active, non-deleted users within a specific system as defined by the SystemId in the ProfileTailorContext. It performs a calculation and saves the static SoD validations for each user, streamlining the process of ensuring that access rights are appropriately segregated among employees.

**Examples Scenario:**

Imagine a scenario where an employee in the finance department also has the access rights to approve vendor payments in the procurement system. Enabling this parameter would help in identifying such risky access combinations across different systems, flagging them for review or remediation.

**Related Settings:** 

- `SapConnectorReadSM20ForEachApplicationServer`
- `CreateApprovalGroupForCompanyEmployeeRecord_QueryActiveDirectoryForEachManager`

**Best Practices:** 

- **configure when:** You have a complex IT environment with employees having access across multiple systems, especially in sensitive areas like finance, HR, and operations.
- **avoid when:** Your organization operates on a single system or has a very small workforce, where manual SoD checks are manageable and not resource-intensive.