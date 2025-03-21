**Include Users Without Risks In Matrix Report**

**Technical Name:** IncludeUsersWithoutRisksInMatrixReport

**Category:** Reporting

**Default Value:** Not explicitly mentioned in the code references, but related settings default to "True"

**Impact Level:** Medium

**Description:**

This parameter controls whether users without identified risks are included in the SoD (Segregation of Duties) Violations Matrix Report within the Pathlock Cloud GRC platform. It ensures comprehensive reporting by allowing visibility into all users, not just those with detected risks.

**Business Impact:**

Including users without risks in matrix reports can provide a complete overview of the system's risk posture, helping to identify potential areas where risk detection may need improvement. It can also support audit and compliance efforts by demonstrating the thoroughness of risk management processes.

**Technical Impact when configured:**

When enabled, reports will include users who have not been flagged with risks, leading to more detailed and extensive reporting. This can be useful for audits and compliance checks, as it demonstrates the organization's commitment to thorough risk analysis and management.

**Examples Scenario:**

- **Audit Preparation:** In preparation for an external audit, the GRC team decides to include users without risks in their reports to show the auditors a full picture of the organization's risk management efforts, including the scope of users assessed.
- **Compliance Review:** During a compliance review process, the organization needs to verify that all users, regardless of their current risk status, have been evaluated for potential SoD violations. This setting ensures that the report reflects this comprehensive evaluation.

**Related Settings:**

- ReportWithBusinessRulesHideInvalidRows

**Best Practices:** 

- **Configure when:** Preparing for audits or compliance reviews where a complete picture of risk management efforts is necessary. It is also useful for internal reviews focused on ensuring all users have been evaluated for risks.
- **Avoid when:** Reporting needs to be streamlined to focus only on users with identified risks to quickly address and mitigate these issues without the noise of clean records.