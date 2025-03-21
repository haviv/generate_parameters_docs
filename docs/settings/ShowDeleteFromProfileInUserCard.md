**Show Delete From Profile In User Card**

**Technical Name:** ShowDeleteFromProfileInUserCard

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ShowDeleteFromProfileInUserCard` parameter determines whether the option to delete information from a user's profile is displayed in the User Card interface within the Pathlock Cloud GRC platform. This setting enhances user profile management by providing administrative control over the visibility of deletion capabilities.

**Business Impact:**

Enabling this feature allows administrators to streamline the user profile interface by potentially removing the delete option, reducing the risk of accidental deletion of critical user information. This can improve data integrity and compliance by ensuring that essential user details are not removed without proper oversight.

**Technical Impact when configured:**

When configured to show the delete option, users with the appropriate permissions can easily remove information from their profiles. Conversely, hiding this option can prevent unauthorized or accidental modifications, bolstering the security and reliability of user data management.

**Examples Scenario:**

- An administrator wants to prevent general users from accidentally deleting important details from their profiles during routine updates. By disabling `ShowDeleteFromProfileInUserCard`, the delete option is hidden, mitigating potential data loss.

**Related Settings:**

- `ExternalDnsForPortalOnly`

**Best Practices:** Configure to show when users have a clear understanding and need to manage their profile information independently. Avoid showing this option when the user base is large or consists of roles that should not modify their profile data unchecked, to maintain data integrity and compliance standards.