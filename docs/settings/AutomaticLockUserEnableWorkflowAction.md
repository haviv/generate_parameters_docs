# Automatic Lock User Enable Workflow Action

**Technical Name:** AutomaticLockUserEnableWorkflowAction

**Category:** User Management

**Default Value:** Not specified

**Impact Level:** High

**Description:**

This parameter is used to enable the automatic locking of user accounts based on specific criteria such as prolonged inactivity or other system-specific settings.

**Business Impact:**

Enabling this parameter helps to enhance security by ensuring that only active and authorized users have access to sensitive information and systems. It reduces the risk of unauthorized access from dormant accounts.

**Technical Impact when configured:**

When configured, it automatically locks user accounts that meet the defined criteria, reducing administrative overhead and strengthening compliance and security postures. It may also notify administrators or other designated contacts about the locking action for audit and monitoring purposes.

**Examples Scenario:**

- A user has not logged into the system for a pre-defined period, triggering the automatic lock to prevent unauthorized use of the inactive account.
- An account is automatically locked after failing to meet the updated security requirements set by the system administrators.

**Related Settings:**

- `NotLockingUsersGroup`: Specifies user groups exempt from automatic locking.
- `AdditionalAdminMailRecipients`: Designated contacts to be notified when an automatic locking action occurs.

**Best Practices:** 

- **Configure when:** You have clear policies for user account inactivity and wish to automate compliance with these policies.
- **Avoid when:** Users frequently have legitimate reasons for extended periods of inactivity or if such automation could disrupt business operations without proper exceptions in place.