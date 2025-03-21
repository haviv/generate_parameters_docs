# Active Directory Account Disable Only

**Technical Name:** ActiveDirectoryAccountDisableOnly

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ActiveDirectoryAccountDisableOnly` parameter controls whether the system performs actions limited to disabling Active Directory accounts. It is relevant in contexts where automated processes adjust user account statuses based on specific triggers or conditions, focusing solely on disabling operations rather than enabling or creating new accounts. 

**Business Impact:**

Implementing this parameter can significantly enhance security measures within an organization by promptly disabling accounts deemed risky, compromised, or no longer in use, without performing any other modifications to the user account attributes. This helps in minimizing potential security breaches and maintaining compliance with internal and external security policies. 

**Technical Impact when configured:**

When the `ActiveDirectoryAccountDisableOnly` parameter is configured, the system restricts its operations to disabling Active Directory user accounts. Any automated task or workflow intending to modify Active Directory user accounts will be limited to the disable action, ensuring that accounts can be promptly deactivated in response to compliance or security events without affecting other user attributes or account status.

**Examples Scenario:**

- **Compliance Requirement:** For compliance with internal security protocols, an organization may require that any employee account that has not been used for 90 days be automatically disabled. By configuring the `ActiveDirectoryAccountDisableOnly` parameter, the system will ensure that such accounts are disabled, adhering to the policy without removing the accounts or altering other attributes which may be necessary for audit purposes.

**Related Settings:**

- `ActiveDirectoryEmployeeIdMinimumLength`
- `AuthorizationRequestMaximumNumberOfMultipleRows`

**Best Practices:** 

- **Configure when:** There's a specific regulatory or business requirement that necessitates the disabling of user accounts based on certain events or conditions, without the need for additional account modification actions.
- **Avoid when:** The operational requirements include automatic user account re-enabling, creation, or attribute modification. This parameter should not be applied in scenarios where a broader range of automated Active Directory account management operations is required.