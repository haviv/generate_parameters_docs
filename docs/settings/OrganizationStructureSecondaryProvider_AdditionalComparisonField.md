# Organization Structure Secondary Provider Additional Comparison Field

**Technical Name:** OrganizationStructureSecondaryProvider_AdditionalComparisonField

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures an additional field for comparison purposes when syncing organizational structures using a secondary data provider. It ensures that the data alignment between primary and secondary sources is accurate and consistent, enhancing data integrity in the synchronization process.

**Business Impact:**

Improper configuration of this parameter could lead to inconsistencies in the organizational structure data sync, affecting reporting, access controls, and potentially leading to security and compliance issues.

**Technical Impact when configured:**

When properly configured, this parameter will enable the platform to accurately match and synchronize data from the primary and secondary providers, ensuring that the organizational structure within the Pathlock GRC platform is current and reflects the actual structure of the organization.

**Example Scenario:**

A company uses an HR system as the primary provider for organizational data and a secondary system for contingent workers. The `OrganizationStructureSecondaryProvider_AdditionalComparisonField` could be set to a unique identifier that exists in both systems, such as employee ID, to ensure that records are accurately matched and updated in the Pathlock GRC platform, reflecting all organizational changes comprehensively.

**Related Settings:**

- `OrganizationStructureProvider_Secondary`

**Best Practices:** configure when the default comparison fields do not adequately match records between your primary and secondary data providers. Avoid when the existing fields already ensure accurate data synchronization.