# Additional Data Extractor Tables For Sync Org

**Technical Name:** AdditionalDataExtractorTablesForSyncOrg

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls additional data tables that are considered during the synchronization process of an organization within the Pathlock Cloud GRC platform. It is intended to ensure that specific, possibly custom, data tables relevant to the organization's security, risk, and compliance data are included in synchronization operations.

**Business Impact:**

Including additional tables for synchronization can have a direct impact on the accuracy and completeness of data used for compliance and risk assessment reports. It ensures that all necessary information is considered when generating compliance statuses, risk assessments, and other reports, which in turn affects decision-making processes and audit outcomes.

**Technical Impact when configured:**

When this parameter is configured, the system includes the specified additional data tables in its synchronization processes. This means that any changes in these tables, or their contents, are reflected in the synchronization outcome, potentially altering the data set used for compliance and risk evaluations.

**Examples Scenario:**

For instance, if an organization has custom tables related to specific regulatory requirements or internal control data not covered by the default synchronization process, configuring this parameter to include those tables ensures that the organization's compliance status reflects all relevant data.

**Related Settings:** 

- `DisableCalcLocalTimeZoneForEntities`
- `ImpactAnalysisShowOtherOptionInSelectionBox`

**Best Practices:** configure when you have additional custom tables that need to be considered in the organization's GRC process, avoid when your data requirements are fully covered by the default table set to prevent unnecessary data processing and complexity.