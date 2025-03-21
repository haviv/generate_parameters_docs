# SoD Review Every Months

**Technical Name:** SoDReviewEveryMonths

**Category:** SOD

**Default Value:** 

**Impact Level:** High

**Description:**

The "SoD Review Every Months" parameter specifies the frequency, in months, at which Segregation of Duties (SoD) violations reviews should be conducted within the Pathlock Cloud GRC platform. This setting is fundamental for maintaining continuous compliance and managing risk efficiently.

**Business Impact:**

Regular reviews of SoD violations help in identifying and mitigating risks related to access controls and potential fraudulent activities. It ensures that no employee or system account holds access rights that, when combined, could lead to unauthorized or undesirable actions within the system. Regular checks are critical for compliance with regulatory standards and internal policies.

**Technical Impact when configured:**

When configured, this parameter automates the scheduling of SoD violations review cycles. It streamlines the compliance process by periodically generating reports or alerts for review, based on the defined cycle. Ensuring timely reviews helps in minimizing risk exposure and enhances the organization's security posture.

**Examples Scenario:**

- An organization configures the "SoD Review Every Months" to 3 months for critical systems. This ensures that every quarter, SoD violations are reviewed and addressed, keeping the access permissions within secure and compliant limits.
- In preparation for an annual audit, a company sets the review cycle to 1 month to rigorously identify and mitigate any SoD violations, demonstrating a proactive approach to compliance and risk management.

**Related Settings:** EnableAsyncApprovalForSodCheckStep

**Best Practices:** 

- **Configure when:** You have a clear understanding of your organizational risk tolerance and regulatory requirements. Setting the review frequency to match these factors ensures compliance and optimal risk management.
- **Avoid when:** There is insufficient resource or infrastructure to support the review process at the configured frequency. Overloading your compliance team or system can lead to oversight and burnout.