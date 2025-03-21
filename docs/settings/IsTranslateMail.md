# Conversion rule of MS Active Directory user email addresses:

**Technical Name:** IsTranslateMail

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**
The `IsTranslateMail` parameter is utilized within the Pathlock Cloud GRC platform to dictate whether email addresses pulled from Microsoft Active Directory should undergo a conversion process. This parameter ensures that email addresses are correctly formatted and standardized for further processing within the platform, facilitating communication and user identification processes.

**Business Impact:**
Setting this parameter affects how user email addresses are managed and recognized across the GRC platform. Correct configuration helps in maintaining accurate user records, reduces the risk of miscommunication, and supports compliance requirements by ensuring that user identities are consistently handled.

**Technical Impact when configured:**
- **Correct Email Format:** Ensures that email addresses are in the right format for internal systems, aiding in communication and notifications.
- **Integration Readiness:** Prepares user data for seamless integration with other enterprise systems requiring standardized email formats.
- **User Identification Accuracy:** Enhances the accuracy of identifying users across the platform, crucial for auditing, reporting, and security operations.

**Example Scenario:**
In an organization where the Active Directory user email addresses are not in a standardized format required by Pathlock Cloud GRC platform, enabling and configuring `IsTranslateMail` will automatically convert the email addresses to the required format. This could be critical in situations where email addresses from Active Directory include domain-specific postfixes or prefixes that need to be standardized for uniformity across enterprise applications.

**Related Settings:**
- `ActiveDirectoryEmployeeIdFormatValue`
- `SapEmployeeIdReplaceString`

**Best Practices:** 
- **Configure when:** There is a necessity to harmonize the email addresses imported from Active Directory with the standardized format required by the Pathlock Cloud GRC platform.
- **Avoid when:** All Active Directory user email addresses already meet the platform's required format or when email modifications could disrupt existing integrations or user identification protocols.