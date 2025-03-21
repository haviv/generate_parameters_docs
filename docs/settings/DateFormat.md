# Date Format

**Technical Name:** DateFormat

**Category:** Configuration

**Default Value:** yyyyMMdd

**Impact Level:** High

**Description:**

The DateFormat parameter specifies the format used to represent dates within the Pathlock Cloud GRC platform, specifically when interfacing with SAP systems. It determines how dates are formatted and interpreted during data extraction and report generation tasks involving SAP logs.

**Business Impact:**

Ensuring the DateFormat parameter is correctly configured is crucial for accurate data synchronization between SAP systems and the Pathlock Cloud GRC platform. It impacts the platform’s ability to correctly interpret and display date information, which is vital for auditing, compliance tracking, and risk management processes.

**Technical Impact when configured:**

When the DateFormat parameter is configured correctly, it ensures that all dates extracted from SAP logs and used in reports are accurately represented, which prevents data inconsistencies. Misconfiguration might lead to incorrect date representations, leading to potential compliance issues or misinterpretations of data during audits.

**Examples Scenario:**

For instance, if the platform is configured to use the default "yyyyMMdd" format, a date like December 1st, 2021, should be entered and displayed as "20211201". This uniformity ensures clarity and precision in reports such as DynamicSoxUserViolationsDetails, which tracks user compliance against specific rules.

**Related Settings:**

- EmptyDate
- TimeFormat

**Best Practices:** configure when setting up integration with SAP systems to ensure data consistency; avoid when data sources use non-standard date formats that could lead to parsing errors or misinterpretations.
