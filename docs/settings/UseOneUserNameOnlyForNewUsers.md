# Use One User Name Only For New Users

**Technical Name:** UseOneUserNameOnlyForNewUsers

**Category:** User Management

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:** This parameter determines whether a single username should be applied across multiple systems when creating new users. If enabled, it ensures consistent usernames across the board, simplifying user management and security audits.

**Business Impact:** Streamlining user identification can significantly reduce the complexities of managing access rights, improve security postures by making it easier to track user activities across different systems, and increase efficiency in onboarding processes.

**Technical Impact when configured:** When this parameter is enabled, during the user creation process across multiple systems, the same username will be used, which simplifies the integration and management of user accounts. This parameter works in tandem with the system's ability to handle single sign-on (SSO) and unified identity management strategies.

**Example Scenario:** A new employee needs access to several systems (e.g., CRM, email, HR portal) as part of their onboarding process. By enabling this parameter, the organization can ensure that the employee uses the same username across all platforms, facilitating a smoother integration into the company's IT infrastructure.

**Related Settings:** CheckUsernameInAllCuaSystems (a setting determining if the username check should be performed across all CUA systems to ensure uniqueness and consistency)

**Best Practices:** 
- **Configure when** initializing systems with multiple user account requirements to ensure consistency and simplify management.
- **Avoid when** different systems require distinct naming conventions that could conflict with implementing a universal username policy.