# Create New User Action Text

**Technical Name:** CreateNewUserActionText

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `CreateNewUserActionText` parameter is used within the Pathlock Cloud GRC platform to define the action text for creating new users in the system. This parameter is crucial for ensuring clear and understandable action descriptions within workflow automations, particularly in the user creation process. It ensures that the actions taken are well documented and easily interpretable by end users and system administrators.

**Business Impact:**

Proper configuration of this parameter enhances user understanding and system transparency during the user creation process. It directly impacts how users and administrators perceive and interact with workflow actions, making the process more intuitive and reducing the risk of errors or misunderstandings.

**Technical Impact when configured:**

When correctly set, the `CreateNewUserActionText` parameter ensures that the action of creating a new user is accurately described within workflow notifications and logs. This contributes to better audit trails, easier troubleshooting, and enhanced user experience by providing clear and concise descriptions of the actions performed within the system.

**Examples Scenario:**

- A system administrator creates a new user account for a recently hired employee. The `CreateNewUserActionText` is displayed as "Initiate New User Onboarding" in the workflow action log, clearly indicating the action taken.
- After an HR manager approves a new employee onboarding request, the action reflected in the system's log, powered by the `CreateNewUserActionText`, reads "Finalize Employee System Integration", offering immediate context about the onboarding stage and action executed.

**Related Settings:** N/A

**Applicable Workflows Actions:** CreateNewUser

**Best Practices:** 

- **Configure when:** Setting up the user creation workflows to ensure that the action texts are clear, precise, and reflective of the action being taken.
- **Avoid when:** Too much detail might confuse end users or when the action descriptions do not align with the standard terminology used in your organization.