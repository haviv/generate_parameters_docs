# Show User Group

**Technical Name:** ShowUserGroup

**Category:** User Management

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** The ShowUserGroup parameter controls the visibility of user group information within various reports and UI elements in the Pathlock Cloud GRC platform.

**Business Impact:** Enabling this parameter can enhance visibility into users' group affiliations, aiding in more efficient user management and audit processes. It allows administrators and auditors to better understand the distribution of users across different groups within the organization, facilitating improved security and compliance with organizational policies and external regulations.

**Technical Impact when configured:** When enabled, the ShowUserGroup parameter triggers the inclusion of user group data in applicable reports and user interface elements, enhancing the comprehensiveness of user-related information presented to administrators and auditors. This can lead to improved decision-making regarding user access rights and group memberships.

**Examples Scenario:** An organization needs to audit user access as part of their compliance with regulatory standards. By enabling the ShowUserGroup parameter, the reports generated will include user group information, allowing auditors to quickly identify and assess user access rights based on group memberships, thereby streamlining the audit process.

**Related Settings:** 

- ShowUserInvalidDateColumn
- ShowSapCompanyColumn
- ShowNumberOfUsers
- ShowUserType

**Best Practices:** 

- **Configure when:** There is a need to enhance visibility into user group memberships for security, compliance, or user management purposes.
- **Avoid when:** Additional user group data in reports or UI elements may lead to information overload or if the organization's governance policies restrict the display of such information for privacy or security reasons.