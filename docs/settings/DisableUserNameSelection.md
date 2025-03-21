# Disable User Name Selection

**Technical Name:** DisableUserNameSelection

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:** The DisableUserNameSelection parameter controls whether users can select usernames during certain operations, such as creating or editing user profiles. When enabled, it restricts the ability to choose usernames, potentially automating or standardizing username creation based on predefined rules or patterns.

**Business Impact:** Enabling this parameter can help maintain a consistent naming convention across user accounts, reducing administrative overhead and improving security by preventing the creation of easily guessable usernames. It may also streamline user onboarding processes by eliminating the step of choosing a username.

**Technical Impact when configured:** Once enabled, the system will bypass any user interface elements or processes that allow for manual username selection. This might affect forms, scripts, or workflows that rely on user input for username selection.

**Examples Scenario:** An organization implements a policy requiring all usernames to follow a specific format, such as "firstnamelastname.department". By enabling DisableUserNameSelection, they ensure that all new user accounts adhere to this format automatically, without requiring manual input or the chance of non-compliance.

**Related Settings:** Not applicable.

**Best Practices:** Configure when you have a clear, organization-wide username policy that you wish to enforce automatically. Avoid when flexibility is needed in username creation, or if username selection is an integral part of your user management or onboarding processes.