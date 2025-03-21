# Active Directory Provider Calculate Employment Status Based On ADStatus

**Technical Name:** ActiveDirectoryProviderCalculateEmploymentStatusBasedOnADStatus

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the employment status of a user within Pathlock's GRC platform is automatically calculated based on their status in Active Directory. When enabled, it uses the custom field specified for termination date in Active Directory to determine if a user's employment status should be marked as terminated or active.

**Business Impact:**

Enabling this feature can significantly improve the accuracy of user employment statuses within the GRC platform, leading to better compliance and risk management outcomes by ensuring only current employees have access to sensitive systems and information.

**Technical Impact when configured:**

When configured, this parameter triggers the system to check the designated custom termination date field in Active Directory for each user. If the current date is beyond the termination date specified in Active Directory, the user's status in the Pathlock platform will automatically be marked as terminated, restricting their access to the platform and any integrated systems.

**Example Scenario:**

A company has an employee who is set to leave the company on December 31st. The IT administrator enters this termination date in the employee's Active Directory profile. With the ActiveDirectoryProviderCalculateEmploymentStatusBasedOnADStatus parameter enabled, once the termination date passes, the employee's status in the Pathlock GRC platform is automatically updated to "terminated," ensuring they no longer have access to any of the platform's functionalities or any connected systems.

**Related Settings:**

- `CustomTerminateDateFieldinActiveDirectory`

**Best Practices:** 

- **Configure when**: Accurate employment status reflecting in real-time in the Pathlock GRC platform is essential for security and compliance. Especially useful in large organizations where manual updates are prone to delays or errors.
  
- **Avoid when**: Your organization's employment status management does not rely on Active Directory statuses, or if the termination dates are not reliably updated in Active Directory.