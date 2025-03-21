# New Username Check All Systems

**Technical Name:** NewUsernameCheckAllSystems

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The New Username Check All Systems parameter is designed to enforce checks across all connected systems during the user creation process. It ensures that a new username is unique and does not already exist in any of the systems to prevent duplicate identity issues and potential security breaches.

**Business Impact:**

Implementing this parameter helps maintain consistency and integrity of user accounts across the entire IT ecosystem. It minimizes the risk of credential overlaps, which can lead to unauthorized access or identity confusion, thus enhancing overall security posture and compliance with identity management policies.

**Technical Impact when configured:**

When configured, this parameter filters through all systems connected to the Pathlock platform to validate the uniqueness of a new username before proceeding with the user creation process. It prevents the addition of a new user if the username is found in any system, ensuring consistent identity management.

**Examples Scenario:**

A new employee is being onboarded and assigned a standard username based on their name. The New Username Check All Systems parameter ensures that this username is not already in use in any of the various systems (HR systems, email, ERP, etc.) managed by Pathlock, avoiding possible conflicts or security issues.

**Related Settings:** NewUsernameForbiddenCharactersReplacement

**Applicable Workflows Actions:**

UserCreationManagement

**Best Practices:** configure when implementing new user creation workflows to ensure universal application of username policies. Avoid using when systems require specific or localized username management practices.