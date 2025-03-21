**Technical Name:** TechnicalNameForDaysUntilExpiration

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:**

This parameter is used to define the number of days until a user's account expires in the system. It is a critical setting in managing user lifecycles and ensuring that access is granted for an appropriate period.

**Business Impact:**

Setting an appropriate expiration date for user accounts helps organizations ensure that access rights are automatically revoked when no longer needed or when an employee leaves the organization. This minimizes the risk of unauthorized access and helps in maintaining a secure and compliant environment.

**Technical Impact when configured:**

When configured, this parameter automatically sets the expiration date for a new user account or updates the expiration date for existing accounts. This helps in automating the process of access deprovisioning, reducing the manual effort required and minimizing the risk of oversight.

**Examples Scenario:**

- **Onboarding New Employees:** When new employees are added to the system, setting the TechnicalNameForDaysUntilExpiration ensures their access is automatically limited to their tenure's duration.
  
- **Contractors:** For temporary staff or contractors, configuring this parameter helps ensure that their access is revoked automatically at the contract's end without manual intervention.

**Related Settings:**

- TerminateNonRequestedSystems: Indicates whether systems not explicitly requested by the user should be terminated upon expiration.

**Best Practices:**  

- **Configure when:** Setting up new user accounts or reviewing existing ones to ensure their access duration aligns with their role and current status within the organization.
  
- **Avoid when:** Indefinite access is required by the user due to their role or responsibilities. In such cases, regularly review the access privileges to maintain security and compliance.