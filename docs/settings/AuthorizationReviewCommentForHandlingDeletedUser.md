# Authorization Review Comment For Handling Deleted User

**Technical Name:** AuthorizationReviewCommentForHandlingDeletedUser

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used in the context of handling workflows related to deleted users within the Pathlock Cloud GRC platform. It allows for specifying comments or notes associated with authorization reviews when addressing or closing out instances related to users that have been removed or deleted from the system.

**Business Impact:**

Implementing this parameter ensures a clear audit trail and documentation for actions taken on workflows associated with deleted users. It supports compliance and governance by providing detailed context on how such instances are handled, which is crucial for internal audits and regulatory scrutiny.

**Technical Impact when configured:**

When properly configured, this parameter enhances the workflow management system by enabling administrators or authorized personnel to annotate specific actions or decisions made regarding deleted user instances. This can aid in the clarity of process actions, decisions rationale, and future reviews of similar incidents.

**Examples Scenario:**

An administrator uses this parameter to add a comment explaining why a particular authorization workflow related to a deleted user was closed without action, such as "User was terminated on [date], and no further access removal is necessary."

**Related Settings:**

- CustomMethodExternalCommandTimeoutInSeconds
- MixedWindowsSecondaryDomainName

**Best Practices:** configure when annotations or explanations are required for audit purposes and compliance reporting; avoid when the workflow handling deleted users does not require additional context or when such information is tracked elsewhere.