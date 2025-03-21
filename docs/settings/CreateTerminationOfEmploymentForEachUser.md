# Set termination of employment for each user:

**Technical Name:** CreateTerminationOfEmploymentForEachUser

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

Configures automated termination processes for employees within the Pathlock Cloud GRC platform. This functionality enables organizations to effectively manage user lifecycles by setting triggers for user terminations based on pre-defined conditions, ensuring compliance with organizational policies and external regulations.

**Business Impact:**

Ensures that the organization's user access rights are up-to-date and compliant with security policies by automatically terminating access rights for employees who have left the organization. This reduces the risk of unauthorized access and potential security breaches, thereby maintaining the integrity of the organization's data security.

**Technical Impact when configured:**

Automates the process of terminating user accounts and revoking access rights within the system, reducing the manual workload on IT and HR departments and eliminating the risk of human error in the termination process.

**Examples Scenario:**

A company has a policy of revoking all access rights of employees on their last working day. By setting the `CreateTerminationOfEmploymentForEachUser` parameter, the system automatically triggers the termination process for any employee flagged for termination, ensuring no delay or oversight in revoking access rights.

**Related Settings:**

- `CommonSettings.Default.EmployeesSourceFileName`
- `CommonSettings.Default.ExternalDllsFolder`

**Best Practices:** configure when you have a clear policy on employee termination and access rights management to ensure timely and secure deprovisioning of system access for leaving employees. Avoid when your organization lacks a structured termination process or when manual oversight is preferred due to specific regulatory requirements or business practices.