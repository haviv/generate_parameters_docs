# Organization Structure Secondary Provider Custom HR System

**Technical Name:** OrganizationStructureSecondaryProvider_Custom_HR_SystemId

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The parameter `OrganizationStructureSecondaryProvider_Custom_HR_SystemId` is designed to facilitate the integration of a secondary HR system into the Pathlock GRC platform. This integration is critical for organizations that use more than one HR system to manage their workforce data and need a comprehensive view of their organization structure across diverse systems.

**Business Impact:**

Integrating a secondary HR system via this parameter allows for more accurate risk and compliance assessments by ensuring all employee data is considered, regardless of the primary HR system in use. It enables the Pathlock GRC platform to synchronize and consolidate organizational structure information, leading to improved decision-making and risk management.

**Technical Impact when configured:**

When this parameter is configured, the Pathlock GRC platform will include data from the secondary HR system in its assessments and reports. This configuration ensures that any changes in the secondary HR system are reflected in the organization's unified structure within the platform, thereby enhancing data accuracy and reliability for GRC processes.

**Examples Scenario:**

An organization uses SAP SuccessFactors as its primary HR system but also maintains a custom HR system for contract and part-time workers not captured in the primary system. Setting up the `OrganizationStructureSecondaryProvider_Custom_HR_SystemId` allows the organization to incorporate these additional employees into the Pathlock GRC platform’s security, risk, and compliance frameworks, ensuring no individual is overlooked.

**Related Settings:**

- EmployeesSourceFileName (within CommonSettings)
- InitContextForSecondaryHrProvider

**Best Practices:** configure when, avoid when

- **Configure when:** You have multiple HR systems to manage different segments of your workforce, and you need to ensure that your GRC processes encompass all employees within the organization for accurate risk assessment and compliance reporting.
  
- **Avoid when:** Your organization uses a single HR system to manage all employee data, or if integrating a secondary system does not add significant value to your GRC strategy due to the homogeneous nature of your workforce management processes.