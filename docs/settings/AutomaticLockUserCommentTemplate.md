# Automatic Lock User Comment Template

**Technical Name:** AutomaticLockUserCommentTemplate

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Automatic Lock User Comment Template parameter is used to define the template for comments added automatically when locking a user account. This parameter allows Pathlock administrators to standardize messages or reasons for automatically locking user accounts across the system.

**Business Impact:**

Having a standardized comment template for automatically locked user accounts helps in maintaining clear and consistent communication within the system's audit trail. This will assist in compliance and auditing processes by providing transparent reasons for user account status changes, thereby enhancing the organization's security posture and compliance with regulatory requirements.

**Technical Impact when configured:**

When configured, this parameter ensures that every action taken to automatically lock a user account is accompanied by a predefined comment. This comment is logged and can be reviewed in the system's audit trail, contributing to a more secure and compliant user account management process.

**Examples Scenario:**

An organization needs to comply with stringent regulatory requirements that mandate the provision of clear, auditable reasons for any access or status changes to user accounts. By configuring the Automatic Lock User Comment Template, every instance where a user account is automatically locked by the system, for reasons such as failed login attempts or suspicious activity, will include a comment based on the template. This ensures that the organization's compliance requirements are consistently met.

**Related Settings:**

- AuthorizationReviewSystemDetailsLinkVisible
- AutomaticLockUserEnableWorkflowAction

**Best Practices:** configure when

- There is a need for consistency in the reasons provided for locking user accounts automatically.
- The organization is subject to compliance with regulatory requirements that necessitate clear, auditable trails for user account status changes.

avoid when

- The organization prefers personalized, case-by-case comments for each locked user account, rather than a standardized template.