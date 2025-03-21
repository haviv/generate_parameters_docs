# Enable Password Must Not Contain Username

**Technical Name:** NewPasswordRule_Enable_PasswordMustNotContainUsername

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:** This setting ensures that passwords cannot contain the user's username, enhancing the security by preventing easy-to-guess passwords.

**Business Impact:** Implementing this rule significantly improves the security posture of an organization by reducing the risk of unauthorized access due to weak passwords. It forces users to create more complex passwords that are less likely to be compromised, thereby protecting sensitive information and systems.

**Technical Impact when configured:** Once enabled, the system will reject any new password that contains the user's username. This check is performed alongside other password requirements, such as minimum length and forbidden characters.

**Examples Scenario:** If a user attempts to set their password to "johnsmith2023" where their username is "johnsmith", the system will deny this action and prompt the user to choose a password that does not include their username.

**Related Settings:** 

- `NewPasswordForbiddenCharacters` - Specifies characters that cannot be used in passwords.

**Best Practices:** Configure this setting for all user accounts to enforce stronger password creation policies. Avoid disabling this feature unless there is a specific and controlled requirement to do so, in which case alternative security measures should be considered.