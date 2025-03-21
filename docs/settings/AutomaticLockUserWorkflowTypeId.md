# Automatic Lock User Workflow Type

**Technical Name:** AutomaticLockUserWorkflowTypeId

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:**

The Automatic Lock User Workflow Type parameter is used to define the specific workflow type for automatically locking user accounts in the Pathlock Cloud GRC platform. This parameter is crucial for ensuring that user accounts that meet certain criteria, such as being inactive for a specified period or failing to comply with HR record requirements, are automatically locked to prevent unauthorized access and maintain system security.

**Business Impact:**

Configuring this parameter helps in enforcing security policies by automatically disabling accounts that are not in use or do not meet the organization's compliance standards. It minimizes the risk of security breaches through dormant accounts and ensures compliance with internal and external audit and regulatory requirements.

**Technical Impact when configured:**

When configured, the system will automatically lock user accounts based on the defined criteria such as inactivity or lack of HR records. This reduces the administrative overhead of manually reviewing and disabling accounts, and enhances the security posture by ensuring only active, compliant accounts have access.

**Examples Scenario:**

- To mitigate the risk associated with dormant accounts, an organization configures the Automatic Lock User Workflow Type to lock user accounts that have been inactive for more than 90 days.
- An organization wishes to ensure compliance with HR policies by locking accounts of users who do not have corresponding HR records, thus configuring the Automatic Lock User Workflow Type accordingly.

**Related Settings:**

- `IncludeOnlyUsersWithHRRecordInLockProcess`: Ensures that only users with corresponding HR records are considered for automatic locking.
- `AdditionalAdminMailRecipients`: Configures additional administrative recipients to be notified when an account is automatically locked.

**Best Practices:** configure when you wish to enhance system security and ensure compliance by automatically managing account lifecycles. Avoid configuring in a manner that is too restrictive without considering the operational impact on users who may be temporarily inactive or awaiting HR record updates.