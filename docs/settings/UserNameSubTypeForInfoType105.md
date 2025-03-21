**Technical Name:** UserNameSubTypeForInfoType105

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter is used to classify users based on their employment status, special payment status, or customer-specific status within the Pathlock Cloud GRC platform's SAP Connector. It indicates how different user types should be processed or categorized, particularly in the context of alternatives to the standard organizational structure.

**Business Impact:** Proper configuration ensures correct identification and categorization of users, which is crucial for enforcing security policies, managing risk, and ensuring compliance across different user groups within the organization.

**Technical Impact when configured:** Enables the Pathlock Cloud GRC platform to accurately process and manage users with specific attributes, ensuring that security and compliance measures are effectively applied based on the user's employment status or special conditions.

**Example Scenario:** For instance, if certain users are on special payment status due to temporary contracts or unique employment conditions, configuring this parameter will help in applying specific compliance and security policies tailored to these user types, enhancing the organization's ability to manage risk and comply with regulatory requirements.

**Related Settings:** 

- `CreateNewUser_DelayAfterCreation`

**Applicable Workflows Actions:** 

**Best Practices:** Configure this parameter when there is a need to differentiate between user types for security, compliance, or management purposes. Avoid using generic settings for all user types to ensure that specific security and compliance measures are adequately enforced.