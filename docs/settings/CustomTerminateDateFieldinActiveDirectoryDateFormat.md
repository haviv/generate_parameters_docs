# Custom Terminate Date Field in Active Directory Date Format

**Technical Name:** CustomTerminateDateFieldinActiveDirectoryDateFormat

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

This parameter configures a custom field to determine the termination date of an employee within the context of integration with Active Directory services. By specifying an Active Directory attribute that holds the termination date, Pathlock GRC platforms can effectively manage user lifecycle events, including de-provisioning access upon employment termination.

**Business Impact:**

Proper configuration of this parameter ensures timely and automated revocation of access rights for terminating employees, mitigating the risk of unauthorized access. This capability is crucial for maintaining security and compliance standards, particularly in environments subject to regulatory requirements regarding access control and data protection.

**Technical Impact when configured:**

When configured, this parameter allows for the automatic update of the employee’s employment status in the Pathlock GRC platform based on the termination date specified in the assigned Active Directory field. This automation streamlines the offboarding process, reducing the workload on IT and HR departments and decreasing the chance of human error.

**Examples Scenario:**

- **Security Compliance:** A financial institution must comply with industry standards requiring all access rights to be revoked within 24 hours of an employee's termination. By using this parameter to automatically trigger access de-provisioning based on the termination date in Active Directory, the institution can easily meet this requirement.

**Related Settings:**

- DirectManagerDynamicApprovalGroupTypeId

**Best Practices:** 

- **Configure when:** Implementation involves frequent employee turnover or when compliance with strict access control policies is required.
- **Avoid when:** The organization does not use Active Directory for employee management or when there is no clear requirement for automated de-provisioning based on termination dates.