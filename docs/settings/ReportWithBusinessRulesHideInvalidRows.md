# Report With Business Rules Hide Invalid Rows

**Technical Name:** ReportWithBusinessRulesHideInvalidRows

**Category:** Reporting

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter determines whether rows that do not comply with defined business rules are hidden in report outputs. When enabled, it filters out invalid data, ensuring that reports only display rows that meet the established criteria, thereby enhancing the accuracy and relevancy of report data.

**Business Impact:**

Enabling this parameter can significantly improve the quality of reports generated for compliance, risk management, and security purposes. It ensures that stakeholders are making decisions based on valid, rule-compliant data, which is crucial in maintaining organizational integrity and achieving compliance with external regulations.

**Technical Impact when configured:**

- Reports generated will exclude rows that fail to meet the predefined business rules, thus reducing clutter and focusing on relevant data.
- It may increase processing time slightly as the system needs to evaluate each row against the business rules before including it in the report.
- Ensures compliance with internal policies and external regulations by only including valid data entries.

**Examples Scenario:**

A compliance officer generates a report to audit user access rights within the system. By enabling ReportWithBusinessRulesHideInvalidRows, the officer ensures that only entries complying with the organization's access control policies are included, automatically filtering out any anomalous or invalid data points that could skew the audit's findings.

**Related Settings:**

- CalculateRoleContentBasedOnMetaActivities

**Best Practices:** 

- Configure when: Accuracy and compliance are critical, especially in reports used for audits, risk assessments, or compliance checks.
- Avoid when: Comprehensive data, including invalid rows, is necessary for analysis or if the additional processing time could impact system performance.