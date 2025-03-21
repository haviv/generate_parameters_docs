# Exclude Locked Activities From SoD

**Technical Name:** ExcludeLockedActivitiesFromSod

**Category:** SOD

**Default Value:** 

**Impact Level:** Medium

**Description:**

The parameter "ExcludeLockedActivitiesFromSod" dictates whether locked activities are omitted from Segregation of Duties (SoD) checks within the Pathlock Cloud GRC platform. This setting is crucial for organizations that require precise control over their security, risk, and compliance postures by refining how SoD violations are identified in relation to system activities that are currently locked.

**Business Impact:**

Including or excluding locked activities in SoD analysis can significantly impact the organization’s risk management strategies. By excluding locked activities, companies can focus on active risks, streamlining compliance efforts and prioritizing areas requiring immediate attention. It affects the accuracy and relevance of SoD violation reports, potentially reducing false positives related to temporarily or permanently locked transactions.

**Technical Impact when configured:**

- When enabled, this setting prevents locked activities from being factored into SoD violation checks, potentially reducing the number of identified violations.
- Helps in refining the scope of SoD reports by excluding locked transactions which are not executable by users, thus focusing on actionable compliance issues.

**Examples Scenario:**

- A financial institution implements this setting to exclude locked activities from its SoD analyses post an ERP upgrade, ensuring the focus remains on active and relevant compliance risks.
- A manufacturing company uses this setting to streamline compliance processes, focusing only on transactions that users can execute, enhancing the effectiveness of audit and compliance activities.

**Related Settings:** 

- `CheckSodForEmployees`

**Best Practices:** 

- **Configure when:** Your organization’s compliance policies demand a focus on active risks or when locked activities are known not to contribute to current risk profiles. It is also advisable to enable this setting following system upgrades or implementations where a substantial number of transactions may be temporarily locked.
- **Avoid when:** Comprehensive risk analysis is required, or all activities, regardless of their status, must be included in the SoD analysis to meet specific regulatory or internal compliance requirements.