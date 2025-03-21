# Check Activity Mode For High Risk Activity Event

**Technical Name:** CheckActivityModeForHighRiskActivityEvent

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

Enables the monitoring and analysis of user activities to identify and flag high-risk events. This parameter is crucial in tracking transactions and activities that could potentially violate security policies or regulatory compliance standards. 

**Business Impact:**

Proper configuration of this parameter helps organizations in mitigating risks associated with unauthorized access, fraud, and compliance violations. It ensures that high-risk activities are promptly identified and addressed, thereby protecting the organization's assets and reputation.

**Technical Impact when configured:**

When enabled, this parameter actively scans and analyzes activities within the system to detect patterns or transactions that are considered high risk based on predefined criteria. It ensures that such activities are flagged for review or further action, enhancing the organization's internal controls and audit trails.

**Examples Scenario:**

1. A user performs a transaction that involves a substantial financial amount, which is not typical for their role. The system flags this as a high-risk activity for further investigation.
2. An employee creates a new vendor account and immediately issues a purchase order, which could indicate potential fraud. The system identifies and reports this sequence of actions as high risk.

**Related Settings:**

- `AuditMinTimeBetweenRequredsInSeconds`
- `CampaignsReviewDetailsTabUARPeerAnalysis`

**Best Practices:** configure when implementing stringent audit controls and monitoring high-risk transactions is essential. Avoid when minimal monitoring is sufficient or in environments where performance impact is a concern.