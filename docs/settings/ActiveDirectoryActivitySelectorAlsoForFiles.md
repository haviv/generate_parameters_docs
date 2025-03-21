# Active Directory Activity Selector Also For Files

**Technical Name:** ActiveDirectoryActivitySelectorAlsoForFiles

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether activities related to file operations within the Active Directory environment should also be considered and tracked by the Pathlock Cloud GRC platform. It enables organizations to fine-tune the scope of activities they monitor for compliance, risk management, and security purposes.

**Business Impact:**

Inclusion of file operation activities in monitoring can significantly enhance the organization's visibility into user behaviors and data handling practices. This can be critical for detecting unauthorized access, data breaches, or non-compliant actions that could lead to financial losses, legal challenges, or reputational damage.

**Technical Impact when configured:**

When enabled, the Pathlock Cloud GRC platform will extend its monitoring capabilities to include file access, modifications, and other file-related activities performed in the Active Directory. This ensures a comprehensive overview of user activities and enhances the organization’s ability to enforce security policies, comply with regulations, and mitigate risks associated with file handling.

**Examples Scenario:**

- A company must adhere to stringent data handling and privacy regulations, such as GDPR or HIPAA. By enabling this parameter, the organization can monitor and audit file-related activities to ensure compliance and quickly address potential violations.
- An organization wants to enhance its insider threat detection capabilities. By tracking file operations, the company can identify unusual access patterns or unauthorized data modification attempts, facilitating timely intervention.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** configure when needing comprehensive activity tracking across both user and file operations within Active Directory environments. Avoid when unnecessary, to reduce data volume and processing overhead.
