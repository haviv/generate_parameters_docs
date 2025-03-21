**Max Records For Single Report Run**

**Technical Name:** MaxRecordsForSingleReportRun

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:**

This parameter defines the maximum number of records that can be included in a single report run within the Pathlock Cloud GRC platform. It ensures optimal performance and prevents system overload by limiting the size of data exports.

**Business Impact:**

Setting an appropriate limit for this parameter ensures that reports are generated and delivered in a timely manner, enhancing decision-making and operational efficiency. It prevents the system from being overwhelmed by large report requests, which can lead to delays or crashes, impacting user experience and productivity.

**Technical Impact when configured:**

When configured correctly, it balances the need for comprehensive data analysis with system performance. A too-low value might restrict the information needed for in-depth analysis, while a too-high value can strain system resources, affecting overall platform performance.

**Examples Scenario:**

A compliance officer needs to generate a report containing user permissions across all systems for an annual audit. Setting an appropriate `MaxRecordsForSingleReportRun` ensures the report is processed efficiently, without overloading the system, allowing timely analysis and submission for the audit.

**Related Settings:**

- DataExportLimit
- ReportGenerationTimeout

**Applicable Workflows Actions:** 

**Best Practices:** 

configure when:
- Setting up reports that are expected to return a large volume of data. It's important to estimate the volume of data your reports will generate and adjust the parameter accordingly.

avoid when:
- For smaller, routine reports where data volume is not a concern. In such cases, default settings are usually sufficient and do not require adjustments.