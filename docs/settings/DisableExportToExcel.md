# Disable Export To Excel

**Technical Name:** DisableExportToExcel

**Category:** Reporting

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The `DisableExportToExcel` parameter controls whether users can export reports and data views to Excel. When enabled, this setting prevents the export functionality, supporting data protection and reducing the risk of sensitive information distribution.

**Business Impact:**

Enabling this parameter ensures that sensitive or critical data managed within the Pathlock platform is not easily exported and distributed, enhancing security and compliance with data protection policies. It affects the user's ability to perform ad-hoc data analysis and sharing.

**Technical Impact when configured:**

When configured, this setting disables the "Export to Excel" option across all reports and data views within the Pathlock Cloud GRC platform. It directly impacts data handling capabilities, particularly impacting reporting, data analysis, and audit functions that rely on Excel for data manipulation and distribution.

**Examples Scenario:**

An organization operating under strict data protection regulations, such as GDPR or HIPAA, could configure the DisableExportToExcel parameter to prevent the accidental or unauthorized distribution of sensitive data. This ensures compliance by limiting data exposure to uncontrolled environments.

**Related Settings:** Not Available

**Applicable Workflows Actions:** Not Applicable

**Best Practices:** Configure the DisableExportToExcel setting in environments where data security and compliance are paramount. Avoid enabling this setting if Excel exports are necessary for business operations, reporting, or analysis tasks.