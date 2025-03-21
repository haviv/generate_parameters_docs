# Custom Terminate Date Field in Active Directory

**Technical Name:** CustomTerminateDateFieldinActiveDirectory

**Category:** User Management

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `CustomTerminateDateFieldinActiveDirectory` parameter is designed to specify a custom field in Active Directory (AD) that represents the termination date of a user account. This parameter enables Pathlock Cloud GRC platform users to manage and automate user deprovisioning processes based on the specified termination date, enhancing the security and compliance posture by ensuring timely revocation of access rights.

**Business Impact:**

Proper configuration of this parameter helps organizations prevent unauthorized access to sensitive systems and data by ensuring that user accounts are deactivated or terminated on their stipulated termination dates. It aids compliance with regulatory requirements regarding access control and minimizes the risk associated with stale or orphaned accounts.

**Technical Impact when configured:**

- Automates the process of identifying and deactivating user accounts that have reached their termination dates in Active Directory.
- Reduces manual workload and potential human errors associated with manual account deprovisioning processes.
- Enhances security by preventing ex-employees or contractors from accessing corporate resources post-termination.

**Examples Scenario:**

An organization has a policy that employee accounts should be deactivated within 24 hours post-termination. By configuring the `CustomTerminateDateFieldinActiveDirectory` with the appropriate AD attribute, the Pathlock Cloud GRC platform can automate the identification and deactivation of these accounts, thus adhering to the company policy and reducing the risk of unauthorized access.

**Related Settings:**

- `ActiveDirectoryProviderAdditionalFields`

**Best Practices:** 

- **Configure when:** You have a clear and consistent policy for user account termination and a corresponding attribute in Active Directory that can be used to trigger deprovisioning processes.
- **Avoid when:** Your organization does not use Active Directory as its primary user directory or if termination dates are not stored or inconsistently maintained within AD attributes.