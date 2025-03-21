# SoD Violation Mitigation For User Will Expire Soon Days

**Technical Name:** SodViolationMitigationForUserWillExpireSoonDays

**Category:** Compliance

**Default Value:** Not specified in the provided references.

**Impact Level:** Medium

**Description:** This parameter defines the number of days before a segregation of duties (SoD) violation mitigation assigned to a user is considered as expiring soon. This early notification aims to prompt timely review and action to ensure continuous compliance and mitigate risk.

**Business Impact:** Proactively managing SoD violation mitigations helps organizations maintain compliance with internal and external regulations. It enhances the organization's security posture by ensuring that mitigating controls are timely reviewed and, if necessary, re-evaluated or extended to prevent unauthorized access or fraudulent activities.

**Technical Impact when configured:** Once configured, the system uses this parameter to determine when to trigger notifications or alerts about upcoming expiration of SoD violation mitigations for a user. This facilitates compliance teams in planning and executing necessary actions well in advance, avoiding last-minute rushes or potential breaches in compliance.

**Examples Scenario:** If this parameter is set to 30 days, the compliance or IT security team will receive a notification 30 days before the expiration of an assigned SoD violation mitigation for a user. This allows sufficient time for the team to review the mitigation measure, assess its effectiveness, and take appropriate action—such as extending the mitigation, reevaluating the user's access, or implementing additional controls.

**Related Settings:** Not enough information to deduce related settings from the provided code references.

**Best Practices:** configure when the organization requires an advanced notice period to proactively manage SoD mitigations. Avoid when the compliance process is mature enough to operate effectively without these advance notifications, or when such notifications could lead to an overwhelming number of alerts, causing alert fatigue.