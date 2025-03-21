# Show Validity Date In User Card

**Technical Name:** ShowValidityDateInUserCard

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether the validity dates associated with a user's profile are displayed within the User Card in the Pathlock Cloud GRC platform. Enabling this setting will reveal dates that indicate when a user's account is valid from and until, providing clear visibility on user account lifespan.

**Business Impact:**

Showing validity dates in the User Card has a direct impact on managing compliance and ensuring that user accounts are active only within their designated time frames. This feature aids in preventing unauthorized access due to outdated user credentials and supports audit requirements by easily displaying user account validity periods.

**Technical Impact when configured:**

When enabled, administrators and auditors can quickly access the validity periods of user accounts from the User Card interface without needing to delve into deeper user settings or reports. This simplifies the process of verifying that each user's access aligns with their current role and responsibilities within an organization.

**Examples Scenario:**

A compliance officer needs to verify that no former employees have lingering access to sensitive systems beyond their termination date. By enabling the ShowValidityDateInUserCard parameter, they can easily spot if any user accounts are set to expire after the known termination dates and take appropriate action.

**Related Settings:**

- `SapApplicationServerPostfix`

**Best Practices:** 

- **Configure when:** It's essential to keep track of user access validity for compliance and security purposes. 
- **Avoid when:** Displaying this information might clutter the interface without adding value to particular user groups, such as when user validity is managed through automated processes not requiring manual oversight.