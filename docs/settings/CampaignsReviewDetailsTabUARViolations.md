# Campaigns Review Details Tab UAR Violations

**Technical Name:** CampaignsReviewDetailsTabUARViolations

**Category:** Audit

**Default Value:** True

**Impact Level:** High

**Description:**

This parameter controls the visibility and functionality of the User Access Review (UAR) Violations tab within the campaign review details section. When enabled, it allows auditors and compliance officers to view and act upon violations identified during the User Access Review process, directly within the campaign module of the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this parameter ensures that organizations maintain stringent compliance standards by providing immediate visibility into access violations within the campaign's review process. This visibility supports timely remediation actions, thus reducing the risk of unauthorized access and potential security breaches.

**Technical Impact when configured:**

When this parameter is configured to 'True', it activates the UAR Violations tab in the campaign review details section, making it possible to review, analyze, and address access violations as part of the campaign's auditing and compliance checks.

**Examples Scenario:**

Suppose an auditor is conducting a routine access review campaign for a financial organization to ensure compliance with SOX regulations. By having the Campaigns Review Details Tab UAR Violations enabled, they can efficiently identify any unauthorized access or segregation of duties (SoD) violations among campaign participants. This functionality allows for immediate action to remediate identified violations, thus ensuring that the organization remains in compliance with SOX requirements.

**Related Settings:**

- CampaignsReviewDetailsTabUARHistory
- EnableModernStyleChartInReportDesigner

**Best Practices:** configure when conducting User Access Reviews as part of compliance and audit campaigns, avoid when not actively reviewing or auditing user access as it may unnecessarily complicate the campaign review interface.