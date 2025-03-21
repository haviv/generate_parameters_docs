# Active Directory Company Attribute

**Technical Name:** ActiveDirectoryCompanyAttribute

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:** This parameter specifies the attribute used to define the company information for a user within Active Directory.

**Business Impact:** Proper configuration of this parameter ensures that users are accurately associated with their respective company within the organization's directory, impacting both reporting accuracy and security policy enforcement related to company-specific data access and workflows.

**Technical Impact when configured:** Correctly setting this parameter ensures that automated processes and integrations that rely on company information (e.g., access controls, audit reporting) perform accurately, reducing the risk of unauthorized access and compliance violations.

**Examples Scenario:** 

- **Scenario:** An organization needs to automate access control based on departmental and company affiliations.
  - **Given** that the ActiveDirectoryCompanyAttribute is correctly configured,
  - **When** a user is onboarded in AD with the company attribute set,
  - **Then** the Pathlock Cloud GRC platform will correctly align the user's access permissions based on the company-specific security policies set in the GRC platform.

**Related Settings:** EnableApplyChangesToDerivedRole

**Best Practices:** 
- **configure when:** setting up user sync processes from Active Directory to ensure that company affiliation is captured and utilized for GRC processes.
- **avoid when:** company information is not used for managing access, compliance, or security within the GRC platform, or if another attribute is more appropriate for distinguishing users' company affiliations.