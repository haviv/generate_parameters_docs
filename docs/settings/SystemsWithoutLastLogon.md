# Systems Without Last Logon

**Technical Name:** SystemsWithoutLastLogon

**Category:** Audit

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter identifies Systems within the Pathlock platform that do not have a recorded last logon date for users. It is utilized to monitor system access and user activity, ensuring accurate audit trails and compliance with access policies.

**Business Impact:**

Lack of visibility into user login activities can pose significant security and compliance risks. Systems without a recorded last logon date might indicate unused accounts or potential vulnerabilities, impacting the organization's ability to enforce access policies and detect unauthorized access.

**Technical Impact when configured:**

When configured, this option helps in enhancing security and compliance by identifying and enabling the review of potentially inactive or unauthorized access. This ensures that all user activities are recorded and auditable, reinforcing the integrity of the system's access control and monitoring.

**Examples Scenario:**

- **Audit Preparation:** In preparation for an audit, an administrator can review the list of systems without last logon dates to identify and eliminate unused accounts, thereby simplifying access management and reducing potential audit findings related to account management.
  
- **Security Review:** A security officer reviews systems identified by this parameter to analyze the risk of potential unauthorized access through accounts that do not have login traceability.

**Related Settings:**

- HideLastLogonDate

**Best Practices:** configure when,

- Preparing for compliance audits to ensure all user activities are traceable.
- Reviewing security policies and access controls to eliminate potential vulnerabilities.

avoid when,

- System performance monitoring tools are in place that might be affected by enabling this feature.
- In environments where login frequency is not an indicator of account legitimacy or security standing.