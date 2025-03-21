# Organization Structure Secondary Provider Properties To Update

**Technical Name:** OrganizationStructureSecondaryProvider_PropertiesToUpdate

**Category:** Configuration

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter is used in the Pathlock Cloud GRC platform to specify which properties of the organization structure's secondary provider should be updated during the synchronization process. 

**Business Impact:**

Configuring this parameter correctly ensures that the organization's structure information remains accurate and up to date, reflecting any changes in the secondary provider sources such as HR systems or other organizational management systems. It helps maintain the integrity of data across the organization's GRC processes.

**Technical Impact when configured:**

When this parameter is configured, the system will selectively update the specified properties in the organization's structure from the secondary provider, potentially avoiding unnecessary updates and data processing. This selective update mechanism can lead to more efficient synchronization processes and better overall system performance.

**Examples Scenario:**

An organization uses an HR system as a secondary provider for its organizational structure data. By setting the `OrganizationStructureSecondaryProvider_PropertiesToUpdate` parameter, the organization can specify that only employees’ job titles and departments should be updated during synchronization, ignoring changes to other properties that are less relevant to the GRC platform functionalities.

**Related Settings:**

- OrganizationStructureSecondaryProvider_MainComparisonField

**Best Practices:** configure when you need to update selective information from the secondary provider to improve efficiency and data accuracy. Avoid configuring this parameter without understanding which data fields are critical to your GRC processes as it might lead to outdated or incomplete data being utilized in the platform.