# Employee Extra Attributes Add Escape

**Technical Name:** EmployeeExtraAttributesAddEscape

**Category:** User Management

**Default Value:** ESS_USERS

**Impact Level:** Medium

**Description:**

This parameter is designed to enhance the management of Employee Self-Service (ESS) users by allowing for the addition of extra attributes that can escape predefined constraints. This enables more flexible and dynamic user data handling within the Pathlock Cloud GRC platform.

**Business Impact:**

Improves the efficiency of managing ESS user groups by providing the ability to include additional user attributes. This can enhance user profile accuracy, enable more tailored access control and reporting, and improve overall compliance and governance processes.

**Technical Impact when configured:**

When this parameter is configured, it allows for the insertion of extra attributes into ESS user profiles beyond the default set. This can include custom identifiers, roles, or permissions that are specific to the organization's needs, thereby enhancing the granularity and precision of access control and user management within the Pathlock environment.

**Examples Scenario:**

An organization may need to include a custom role attribute for ESS users that identifies their department or specific access level within certain applications. By configuring the EmployeeExtraAttributesAddEscape parameter, the organization can easily add this custom attribute to their ESS user profiles, improving the accuracy of user data and enabling more precise control over application access based on departmental roles.

**Related Settings:**

None identified as directly related within the provided code references.

**Best Practices:** 

- **Configure when:** You need to add custom attributes to ESS user profiles that are not covered by the default settings, for supporting detailed access control or compliance requirements.
- **Avoid when:** The default ESS user attributes suffice for your organizational needs, to prevent unnecessary complexity in user profile management.