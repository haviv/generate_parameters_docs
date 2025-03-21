# Authorization Review Exclude Locked Users

**Technical Name:** AuthorizationReviewExcludeLockedUsers

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter determines whether locked users should be excluded from authorization review processes. When enabled, users who have been locked out due to security policies or other reasons will not be included in the review process. 

**Business Impact:**

Excluding locked users from authorization reviews can streamline the review process by focusing on active users, reducing the time and effort required for reviews. It also ensures that evaluations are centered on relevant user accounts, which is crucial for maintaining accurate and efficient security and compliance postures.

**Technical Impact when configured:**

When configured to exclude locked users, the authorization review process will skip these accounts, potentially lowering the number of users to be reviewed. This can simplify management tasks and focus security efforts on active accounts, enhancing both security and operational efficiency.

**Examples Scenario:**

A company periodically conducts authorization reviews as part of their compliance requirements. By enabling this parameter, they can ensure that their reviews are more targeted and efficient, as they will not need to consider users who have been automatically locked out due to consecutive unsuccessful login attempts or those who have been manually locked by administrators.

**Related Settings:**

- AuthorizationReviewShowLastLogonDate

**Best Practices:** Enable this setting in environments where user accounts are regularly reviewed for access rights and compliance, and where account lockouts are used as a security measure. Avoid enabling it if locked accounts still require scrutiny during review processes, such as in highly regulated industries where even locked accounts must be audited.