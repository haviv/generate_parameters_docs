# Show SoD Severity Description

**Technical Name:** ShowSodSeverityDescription

**Category:** SOD

**Default Value:** False

**Impact Level:** Medium

**Description:**

The ShowSodSeverityDescription parameter enables the display of the Severity Description for Segregation of Duties (SoD) violations within the Pathlock Cloud GRC platform. When enabled, users can see detailed descriptions of the severity levels associated with SoD violations directly within the relevant interface components, enhancing understanding and facilitating better decision-making regarding risk management.

**Business Impact:**

Enabling this feature provides users with meaningful insights into the potential risks associated with SoD violations by presenting a more descriptive analysis of the severity levels. It supports compliance and audit teams in prioritizing violations that pose the greatest risk to organizational integrity, security, and compliance.

**Technical Impact when configured:**

When configured to true, this setting activates the display of severity descriptions for SoD violations in applicable reports and interfaces within the Pathlock platform, offering users additional details that can guide risk assessment and remediation efforts more effectively.

**Examples Scenario:**

- **Audit Preparation:** Prior to an audit, the compliance team enables ShowSodSeverityDescription to review and prioritize SoD violations based on their severity descriptions. This facilitates targeted remediation of high-severity violations.

**Related Settings:**

- AuthorizationReviewInRequestsWaitingPage

**Best Practices:** 

- **Configure when:** Detailed severity information is needed to enhance the understanding and management of SoD violations, especially in preparation for audits or when assessing and prioritizing risks.
- **Avoid when:** Simplified SoD violation data is sufficient for the organization's compliance and risk management processes, or if the additional information may overwhelm the system users.