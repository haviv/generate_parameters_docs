# Is Display Activity Group Without Type

**Technical Name:** IsDisplayActivityGroupWithoutType

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether activity groups are displayed without their associated types in reporting views. It aims to simplify reports by focusing on the activity groups, disregarding the type of activity being performed.

**Business Impact:**

Enabling this setting can provide a cleaner, more straightforward view of activities in reports, which is particularly beneficial for non-technical stakeholders who require summarized information without detailed transaction types. It facilitates quicker understanding and decision-making based on activity group data alone.

**Technical Impact when configured:**

When this parameter is configured to display activity groups without their associated types, reports generated within the Pathlock Cloud GRC platform will omit the type detail for each activity group. This alteration impacts how data is visualized and can lead to a more streamlined presentation of activity data, significantly affecting the consumption of the reports by end-users.

**Examples Scenario:**

A compliance officer generates a report to review all high-risk activities within a specific period. By enabling this parameter, the report simplifies by only listing the groups of activities, not the specific types within each group. This allows for a quicker assessment of where potential risks are concentrated without the need for detailed transaction type analysis, enhancing the efficiency of the compliance review process.

**Related Settings:**

- TechnicalNameForActivityGroup
- TechnicalNameForActivityMode

**Best Practices:** 

- **Configure when:** You aim to simplify report data for stakeholders who need to understand activity trends without the complexity of detailed transaction types.
- **Avoid when:** Detailed analysis of activities, including the types of transactions, is necessary for technical audits or in-depth risk assessments, where omitting such details may hinder the understanding of the security posture.