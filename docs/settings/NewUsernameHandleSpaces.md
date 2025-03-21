**Technical Name: NewUsernameHandleSpaces**

**Category: User Management**

**Default Value:**

**Impact Level: Medium**

**Description:**

Configures how spaces are handled in new usernames during the user creation process. This setting ensures that usernames conform to specific formatting rules, promoting consistency and preventing issues related to username recognition across various systems.

**Business Impact:**

Improper handling of spaces in usernames can lead to user identification problems, affecting login processes and access rights assignments. Ensuring a standardized username format enhances security protocols and minimizes the risk of unauthorized access or system vulnerabilities.

**Technical Impact when configured:**

When properly configured, this parameter ensures that spaces in new usernames are either removed or replaced based on pre-defined rules. This contributes to a more secure and streamlined user management process, facilitating easier tracking and management of user accounts within the Pathlock GRC platform.

**Examples Scenario:**

A company implements a rule where spaces in usernames must be replaced with a period ('.'). When a new user named "John Doe" is added to the system, the NewUsernameHandleSpaces parameter ensures his username is automatically formatted as "John.Doe", adhering to the company's username policy.

**Related Settings:**

- `CreateNewUserUpdateImmediately`
- `MailListnerApprovedKeywords`

**Best Practices:** configure when standardizing username formats for new users; avoid when individual identity systems require distinct username formats not compatible with global settings.