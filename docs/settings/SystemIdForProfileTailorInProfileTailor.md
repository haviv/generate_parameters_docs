# System Id For Pathlock In Pathlock

**Technical Name:** SystemIdForProfileTailorInProfileTailor

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** The SystemIdForProfileTailorInPathlock parameter is used to identify the system ID specifically for Profile Tailor within the Pathlock GRC platform. This system ID is critical for linking and managing user profiles across the integrated systems within Pathlock.

**Business Impact:** Proper configuration of this parameter ensures seamless integration and management of user profiles, directly affecting the organization's ability to maintain compliance, manage risk, and ensure security across its digital landscape.

**Technical Impact when configured:** When properly configured, this parameter enables the Pathlock platform to accurately identify and manage user profiles, ensuring that the right access controls are applied and that user activities are monitored in compliance with organizational policies and standards.

**Examples Scenario:** 
- **Scenario 1:** An organization wants to ensure that all user profiles are accurately managed across their ERP system integrated with Pathlock. By setting the SystemIdForProfileTailorInProfileTailor parameter, they ensure that user profiles created or modified in the ERP system are accurately reflected and managed within Pathlock, maintaining the integrity of their access control policies.

**Related Settings:**
- DefaultRoleForDirectManager: Determines the default role applied to direct managers, which could be related when considering overarching access control strategies and profile management.

**Best Practices:** 
- **Configure when:** Setting up or integrating new systems within the Pathlock platform to ensure that all user profiles are accurately identified and managed.
- **Avoid when:** There is no clear mapping or understanding of the systems integrated with Pathlock, as improper configuration can lead to mismanagement of user profiles and access controls.