# Custom Role For Auto Complete Prevent For No Role

**Technical Name:** CustomRoleForAutoCompletePreventForNoRole

**Category:** User Management

**Default Value:** ""

**Impact Level:** Medium

**Description:**

The `CustomRoleForAutoCompletePreventForNoRole` parameter is designed to enhance the user management process within the Pathlock Cloud GRC platform. It specifies a custom role that is used to prevent the auto-completion feature from suggesting users who do not have any assigned roles. This ensures that only relevant users are suggested in auto-complete fields throughout the platform, particularly in areas involving workflow management.

**Business Impact:**

Implementing this parameter can significantly streamline user assignment and workflow steps by ensuring that only users with specific roles are considered in auto-complete suggestions. This leads to improved security and efficiency in managing permissions and user access throughout various platform operations.

**Technical Impact when configured:**

Once configured, the auto-complete functionality across the Pathlock Cloud GRC platform will filter out users without roles, based on the specified custom role. This effectively prevents unauthorized or irrelevant user suggestions, thereby enhancing the integrity of user management and workflow operations.

**Examples Scenario:**

- **Before Implementation:** The auto-complete feature suggests all users, including those without any roles, leading to possible misassignments and a cluttered selection process.
  
- **After Implementation:** The auto-complete feature only suggests users who have been assigned the specified custom role, ensuring that only qualified and relevant users are considered for assignment in workflow steps and other areas.

**Related Settings:**

N/A

**Best Practices:** 

- **Configure when:** You have a clear distinction in your user base, where specific roles are required for tasks, and you wish to streamline user selection processes.
  
- **Avoid when:** Your organization does not differentiate users by roles, or all users require equal access and visibility across the platform.