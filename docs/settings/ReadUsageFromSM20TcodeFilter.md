# Read Usage From SM20 Tcode Filter

**Technical Name:** ReadUsageFromSM20TcodeFilter

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

The Read Usage From SM20 Tcode Filter parameter is designed to filter the usage data extracted from the SM20 transaction code logs. This parameter enables organizations to streamline their audit reports by focusing on specific activities or events within their SAP environment, ensuring a more targeted and efficient audit process.

**Business Impact:**

Configuring this parameter with the appropriate filters can significantly reduce the volume of audit data to be analyzed, making it easier for audit teams to identify potential security risks or compliance issues. By filtering out irrelevant data, organizations can also ensure that their audit processes are more focused on areas with higher risk or greater impact on compliance and regulatory requirements.

**Technical Impact when configured:**

- **Increased Efficiency**: Audit reports are generated more quickly due to the reduced volume of data being processed.
- **Improved Focus**: Allows audit teams to concentrate on events that are of genuine concern or interest, enhancing the effectiveness of the audit.
- **Reduced Storage**: Saves on storage costs associated with keeping large volumes of audit log data.

**Examples Scenario:**

An organization wants to monitor and audit the use of high-risk Tcodes in their SAP environment, such as those that can change configuration settings or user permissions. By setting up the Read Usage From SM20 Tcode Filter to include only these high-risk Tcodes, the audit team can efficiently focus their review on activities that pose the highest risk.

**Related Settings:**

- EnableIncludeRiskDescriptionColumnActivitiesMatrixReports

**Best Practices:** 

- **Configure when:** You have specific transactions or activities within SM20 logs that are of primary interest for security, compliance, or audit purposes.
- **Avoid when:** There is a need to capture and analyze all activities without filtering, to ensure no potential issues are overlooked.