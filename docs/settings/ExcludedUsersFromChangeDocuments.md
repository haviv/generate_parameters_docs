# Excluded Users From Change Documents

**Technical Name:** ExcludedUsersFromChangeDocuments

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to specify user accounts that should be excluded from processing or consideration within the scope of Change Document operations within the Pathlock GRC platform. It allows for the filtering out of specific users to ensure their activities are not included in change document-related analyses or reports.

**Business Impact:**

Excluding specific users from change documents can help in focusing compliance and audit efforts on the relevant user base, reducing the noise from system or non-relevant accounts. It ensures that automated operations and reports are more accurate and relevant to the organization's actual risk and compliance posture.

**Technical Impact when configured:**

- Excluded user accounts will not have their activities captured or included in change document reports.
- May reduce the volume of data processed and improve performance for analyses involving change documents.
- Helps in maintaining clarity and relevance in compliance reporting by focusing on pertinent user activities.

**Examples Scenario:**

- Exclude technical or system accounts from change document reports to focus on human user activities.
- Omit users who are known to perform routine maintenance tasks that do not impact compliance or security posture.

**Related Settings:**

SyncronizeEmployeesFieldsToExclude

**Best Practices:** configure when users' activities are known to be irrelevant or misleading for compliance and security analyses; avoid when comprehensive tracking of all user activities is necessary.