# Organization Structure Secondary Provider Main Comparison Field

**Technical Name:** OrganizationStructureSecondaryProvider_MainComparisonField

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter specifies the main field used for comparison when integrating data between the primary organizational structure provider and a secondary provider. It is a critical setting in ensuring data consistency and integrity during the data synchronization process.

**Business Impact:**

The correct setting of this parameter ensures that the organizational hierarchy, including departments, roles, and employee details, is accurately reflected across systems. It prevents data mismatches and ensures that governance, risk, and compliance (GRC) decisions are made based on reliable and consistent information.

**Technical Impact when configured:**

Proper configuration enables seamless integration and synchronization between different HR systems or organizational structure data providers. This ensures that changes in organizational structures are accurately reflected across all connected systems, maintaining data integrity and support for compliance and risk management processes.

**Examples Scenario:**

For instance, if the HR system is considered the primary source of truth for organizational data and a secondary ERP system needs to be synchronized. If "EmployeeID" is the main comparison field, this setting will ensure that the synchronization process matches records based on the "EmployeeID" across both systems, preventing data duplication or inconsistencies.

**Related Settings:**

- OrganizationStructureProvider_Type
- SyncOrganization_DataMapping

**Best Practices:** configure when integrating multiple data sources for organizational structures to ensure data consistency. Avoid complex or non-unique fields as the main comparison field to prevent data integration issues.