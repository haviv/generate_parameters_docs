# Automatic Lock User Never Logged In Text

**Technical Name:** AutomaticLockUserNeverLoggedInText

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter determines the message displayed or action taken when an automatic lock is initiated on users who have never logged in. It is part of the security features aimed at enhancing the control over user access and ensuring that only active and legitimate users have access to the Pathlock Cloud GRC platform.

**Business Impact:**

Implementing this feature can significantly enhance security by automatically disabling or locking out accounts that have never been used. This reduces the risk of compromised credentials and deters the accumulation of dormant accounts, which could potentially be exploited by unauthorized individuals.

**Technical Impact: when configured:**

When configured, this parameter activates the automatic locking mechanism for users who have never logged in, based on the specific conditions set within the platform. It ensures that user accounts are validated and reduces the administrative overhead of manually monitoring and managing user account states.

**Examples Scenario:**

For instance, if a company has a policy of locking out accounts that have been created but never logged in within 30 days, this parameter can be configured to display a specific message indicating the account has been locked due to inactivity. This assists in enforcing security policies automatically without manual intervention.

**Related Settings:**

- AutomaticLockUserEnableWorkflowAction
- AutomaticLockUserWorkflowTypeId

**Best Practices:** configure when aiming to improve security and ensure user account management is automated effectively; avoid when there is a need for accounts to remain active for longer periods without login due to specific business requirements.