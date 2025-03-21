# Disable System Selection Narrow By User Groups

**Technical Name:** DisableSystemSelectionNarrowByUserGroups

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the system narrows down the selection of systems a user can access based on their user group memberships. When enabled, users will see a wider list of systems regardless of their group affiliations, potentially simplifying administration at the cost of finer-grained access control.

**Business Impact:**

Enabling this setting may increase the ease of system access for users, potentially improving workflow efficiency. However, it could also raise security concerns by broadening access to systems that users do not need for their specific roles, possibly violating the principle of least privilege.

**Technical Impact when configured:**

- **Enabled (True):** Users can see and potentially access a broader set of systems, not limited by their user group memberships.
- **Disabled (False):** The system selection for users is narrowly tailored based on the groups to which they belong, enhancing security but requiring more precise group and access management.

**Examples Scenario:**

- A global organization with a large number of systems may choose to disable this setting to ensure that employees only access systems relevant to their department or function, thereby enhancing security and reducing the risk of inadvertent access to sensitive information.
- A smaller company or one with a flat organizational structure may enable this setting to reduce administrative overhead and allow all users simplified access to necessary systems without detailed group membership management.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:** Your organization has robust security measures in place, and you desire to simplify system access for users across various groups.
- **Avoid when:** Your organization relies heavily on restrictive access controls based on group membership to safeguard sensitive information and systems.