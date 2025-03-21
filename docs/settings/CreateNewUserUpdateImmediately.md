# Create New User Update Immediately

**Technical Name:** CreateNewUserUpdateImmediately

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**
The `CreateNewUserUpdateImmediately` parameter controls whether new user accounts are immediately active upon creation within the system. This setting is significant in systems that support or require immediate account provisioning following creation to allow users instant access to necessary resources.

**Business Impact:**
Enabling this parameter ensures that new employees or users can begin their tasks without waiting for manual account activation, leading to a smoother onboarding experience and increased productivity. It is particularly beneficial in dynamic environments where immediate access to systems and applications is crucial.

**Technical Impact when configured:**
When enabled, user accounts are immediately activated upon creation, bypassing any potential delays associated with manual activation processes. This can be critical for maintaining operational efficiency and ensuring that users have access to required systems and tools without delay.

**Examples Scenario:**
- **Scenario:** A new employee joins the company and requires immediate access to the company's project management tool to start on a time-sensitive project. With `CreateNewUserUpdateImmediately` enabled, the employee's user account is created and activated instantly, allowing them to log in and access the project management tool without any delays.

**Related Settings:**
- ConnectUsersToEmployee_ByEmail

**Best Practices:**
- **Configure when:** Immediate access for new users to system resources is required.
- **Avoid when:** The organization's security policy demands a review or waiting period before granting new users access to systems.