**Technical Name:** OrganizationStructureSecondaryProvider_CharsToTrim

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `OrganizationStructureSecondaryProvider_CharsToTrim` parameter is designed to specify the number of characters to trim from the organization structure information received from a secondary provider within the Pathlock Cloud GRC platform. This parameter helps in aligning and managing organizational data accurately by removing extraneous characters that may have been included during data integration from various sources.

**Business Impact:**

Improper configuration of this parameter can lead to discrepancies in organizational structure representation, affecting user access reviews, risk analysis, and compliance reporting. Accurately setting it ensures that the organization's structure is reflected correctly across the platform, thereby supporting effective governance, risk management, and compliance (GRC) processes.

**Technical Impact when configured:**

Correct configuration aids in the precise synchronization of organizational data by avoiding errors related to excess characters. It ensures that secondary provider data matches the primary organizational structure format, facilitating smoother integrations and data management workflows.

**Examples Scenario:**

If an organization receives data from a secondary provider where department codes are prefixed or suffixed with certain characters for internal processing reasons (e.g., "_HR" instead of "HR"), configuring this parameter to trim the relevant characters ensures that the department codes align with the organization’s primary system of record.

**Related Settings:**

- OrganizationStructureSecondaryProvider_AdditionalComparisonField

**Best Practices:** configure when you encounter data integration issues related to organizational structure mismatches, avoid when the secondary provider's data is already in the required format without extra characters.