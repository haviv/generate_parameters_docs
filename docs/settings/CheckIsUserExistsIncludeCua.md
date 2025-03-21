# Check Is User Exists Include Cua

**Technical Name:** CheckIsUserExistsIncludeCua

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

The parameter `CheckIsUserExistsIncludeCua` is utilized to determine whether the system should check if a username exists across all Connected User Administration (CUA) systems. When enabled, this feature expands user existence verification to include all systems integrated with the CUA, offering a comprehensive oversight.

**Business Impact:**

Enabling this parameter ensures thorough vetting of user accounts across all systems, minimizing the risk of duplicate user accounts and unauthorized access. This is critical for maintaining stringent security standards and compliance requirements, particularly in environments where centralized user management is essential.

**Technical Impact when configured:**

When configured to `True`, the system performs an exhaustive search for the user's existence across all systems connected through CUA, rather than limiting the search to the local system. This is particularly significant in distributed system environments where user accounts may span multiple systems.

**Examples Scenario:**

- **Situation:** An organization utilizes multiple systems that are interconnected for centralized user management. To avoid security risks associated with duplicate user accounts, the organization wants to ensure that a user being added does not already exist in any of the connected systems.
- **Action:** The `CheckIsUserExistsIncludeCua` parameter is set to `True` to enable widespread search and verification of user existence across all CUA-connected systems.
- **Outcome:** The system now checks for the existence of the user account across all integrated systems, preventing duplicate account creation and bolstering security measures.

**Related Settings:**

- `AutomaticUserLockOverrideDisableDefaultAction`

**Best Practices:** 

- **Configure when:** You're managing user accounts in an environment with multiple interconnected systems, and it's crucial to prevent the creation of duplicate user accounts across these systems.
- **Avoid when:** Your system operates in a standalone mode or the performance impact of checking multiple systems for user existence outweighs the benefits in your specific context.