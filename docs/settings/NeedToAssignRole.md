# Need To Assign Role

**Technical Name:** NeedToAssignRole

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether a user needs to be assigned a specific role within the Pathlock Cloud GRC platform. It is utilized in scenarios where user roles are dynamically managed based on certain criteria or workflows within the organization.

**Business Impact:**

Ensuring that the correct roles are assigned to users is critical for maintaining the integrity of security, compliance, and risk management processes within an organization. Misassignment could lead to unauthorized access or inability to perform required tasks, impacting operational efficiency and security posture.

**Technical Impact: when configured**

Proper configuration ensures that users receive the appropriate access rights for their role, maintaining the principle of least privilege and supporting compliance with internal and external regulations. It can also streamline the user onboarding process by automating role assignments based on predefined criteria.

**Examples Scenario:**

A new employee in the finance department needs access to sensitive financial reports. With the NeedToAssignRole parameter configured, the system automatically assigns the finance role to the user, granting them the necessary access without manual intervention, thus reducing the time and potential errors associated with manual role assignment.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** configure when new roles are required for specific tasks or compliance requirements are updated. Avoid when users do not require specialized access beyond their current roles.