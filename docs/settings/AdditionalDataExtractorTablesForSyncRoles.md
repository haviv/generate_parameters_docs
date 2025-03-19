**Technical Name:** AdditionalDataExtractorTablesForSyncRoles

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AdditionalDataExtractorTablesForSyncRoles` parameter specifies additional database tables to be included during the synchronization of role data within the Pathlock Cloud GRC platform. This configuration is crucial for ensuring that all necessary data is accounted for in security, compliance, and risk management processes.

**Business Impact:**

Configuring this parameter allows organizations to tailor the data synchronization process to their specific needs, facilitating more comprehensive role analysis and reporting. It ensures that custom or non-standard tables, which may contain critical information for security and compliance, are not overlooked.

**Technical Impact when configured:**

When properly configured, this parameter broadens the scope of data analysis for roles within the system, allowing for a more thorough audit and review process. It enhances the platform's ability to detect potential security risks and compliance issues by considering a wider range of data points.

**Examples Scenario:**

- A financial institution requires synchronization of custom tables containing specific financial transaction roles for audit purposes. By including these tables through the `AdditionalDataExtractorTablesForSyncRoles` parameter, they ensure these roles are considered in compliance checks and risk assessments.

**Related Settings:**

- AuthorizationReviewDisableWideApprovalFilter

**Best Practices:** Configure when additional or custom tables relevant to role data need to be included in the synchronization process. Avoid when the default role synchronization process adequately meets organizational needs, to minimize unnecessary data processing and complexity.