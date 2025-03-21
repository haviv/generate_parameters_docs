**Technical Name:** V2_Rfc_Server_Dest_Records_Columns

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of various columns in the UI related to RFC (Remote Function Call) server destinations and records. By enabling or disabling specific fields, administrators can customize the data presented to the users, focusing on what's relevant for security, auditing, or operational purposes within the Pathlock Cloud GRC platform.

**Business Impact:**

Configuring this parameter allows businesses to tailor the information displayed to users, ensuring that sensitive data is accessible only to those with the requisite permissions. This customization supports compliance with internal policies and external regulations by limiting access to critical data and functionality, thereby reducing the risk of unauthorized access or data breaches.

**Technical Impact when configured:**

When properly configured, this setting enhances the user interface by displaying only the relevant data columns for RFC server destinations and records. This not only simplifies the user experience but also aids in the efficient management of security and compliance data, enabling quicker decision-making and more effective risk management.

**Examples Scenario:**

An administrator needs to ensure that the Pathlock Cloud GRC platform users can only view essential information about the RFC server destinations to prevent overwhelming them with unnecessary data. By configuring the `V2_Rfc_Server_Dest_Records_Columns` parameter, they disable columns like "ShowUserGroup" and "ShowUserType" for a more streamlined and focused user interface.

**Related Settings:**

- ShowLatLogOn
- ShowLocalTime
- ShowMessageOnSystemChange
- ShowRoleTypeColumn
- ShowSapCompanyColumn
- ShowSystemTime
- ShowUserGroup
- ShowUserType

**Best Practices:** configure when you need to streamline the user interface and focus on specific details for better security and compliance management. Avoid when comprehensive data visibility is required for detailed audits and security reviews.