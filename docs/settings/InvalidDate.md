**Invalid Date**

**Technical Name:** InvalidDate

**Category:** Audit

**Default Value:** 1900-01-01

**Impact Level:** Medium

**Description:**

The 'Invalid Date' parameter represents a baseline date used within the Pathlock Cloud GRC platform to validate or flag data entries, specifically focusing on user logon activities and related audit trails. It serves as a threshold to distinguish between valid and potentially invalid or outdated data within user records and system logs.

**Business Impact:**

Incorrect or outdated data can lead to inaccurate reporting and analysis of user activities, potentially masking unauthorized access or non-compliance with internal policies and regulations. Establishing a clear cut-off date helps in maintaining the integrity and reliability of audit trails and user management processes, which is crucial for compliance and security governance.

**Technical Impact when configured:**

When configured, the 'Invalid Date' parameter aids in identifying and filtering out records that fall below the specified date threshold. This helps in cleaning data, improving the performance of audit reports, and ensuring that compliance checks are based on current and relevant data.

**Examples Scenario:**

An organization needs to audit user access logs for the current year but realizes that their system contains historical logs dating back to the early 1900s due to system migrations and legacy data imports. By setting the 'Invalid Date' parameter, they can exclude these irrelevant records from their analysis, focusing instead on pertinent data.

**Related Settings:**

None directly mentioned in the provided code references.

**Best Practices:** configure when establishing or reviewing audit and compliance policies to ensure data relevance and integrity; avoid when historical data is significantly vital for continuous legal or compliance requirements.