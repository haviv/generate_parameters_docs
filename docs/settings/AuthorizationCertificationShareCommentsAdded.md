**Authorization Certification Share Comments Added**

**Technical Name:** AuthorizationCertificationShareCommentsAdded

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

The parameter `AuthorizationCertificationShareCommentsAdded` is used to control whether comments added during the authorization certification process are shared among relevant stakeholders or kept private. This setting is crucial for ensuring that the communication process during the authorization review is in line with the organizational policy on transparency and confidentiality.

**Business Impact:**

Enabling this parameter ensures that comments made during the certification process can be shared, promoting transparency and collaboration among the team members and relevant stakeholders. It helps in creating a clear audit trail and supports decision-making processes by providing context and insights into the decisions made during the authorization certification process.

**Technical Impact when configured:**

When configured to true, any comments added during the authorization certification process will be visible to all stakeholders involved in the process. This facilitates better communication and understanding among the team members. If set to false, the comments will only be available to the person who added them, limiting the visibility and possibly hindering collaboration.

**Examples Scenario:**

- **Scenario 1:** An organization requires that any objections or approvals regarding user access rights during the authorization certification must be fully transparent to audit, compliance, and security teams. Setting `AuthorizationCertificationShareCommentsAdded` to true enables this requirement by ensuring that all comments are shared with relevant stakeholders.
  
- **Scenario 2:** Another organization prefers to keep the reviewers' comments confidential to protect the identities or prevent bias in decision-making. Here, setting `AuthorizationCertificationShareCommentsAdded` to false would ensure that comments are not shared beyond the individual who made them.

**Related Settings:** 

- `RoleBuilder_EnableTransactionsRemoval`

**Best Practices:** configure when transparency and collaboration among stakeholders are required during the authorization certification process; avoid when there is a need to keep the comments private or when confidentiality is a priority.