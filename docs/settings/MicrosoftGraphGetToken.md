# Microsoft Graph Get Token

**Technical Name:** MicrosoftGraphGetToken

**Category:** Configuration

**Default Value:** https://graph.microsoft.com/.default

**Impact Level:** High

**Description:**

The `MicrosoftGraphGetToken` parameter is responsible for specifying the scope of the Microsoft Graph API that Pathlock Cloud GRC platform should communicate with. It defines the set of permissions that the platform has when interacting with Microsoft services through the Graph API.

**Business Impact:**

Configuring this parameter correctly ensures that the Pathlock Cloud GRC platform can securely manage and access Microsoft services, including but not limited to user management, audit logs, and compliance data. Incorrect configuration may lead to insufficient data access or exposure to unauthorized operations.

**Technical Impact when configured:**

- Ensures secure and scoped access to Microsoft services.
- Enables the Pathlock platform to perform operations within the defined scope, thereby supporting compliance, security, and user management workflows effectively.

**Examples Scenario:**

- **Compliance Management:** By setting the scope to include access to compliance data, organizations can automate compliance checks and manage risk assessments directly from the Pathlock platform.
- **User Management:** Configuring the scope to include user management permissions enables organizations to automate user lifecycle operations on Microsoft services through Pathlock.

**Related Settings:**

- WorkflowAutomaticStepsApprovedByText
- WorkflowDeclined
- WorkflowReminderAuthoirizationCertificationFormat
- WorkflowReminderContainer

**Best Practices:** 

- **Configure when:** Setting up Pathlock Cloud GRC platform to interact with Microsoft services. It's crucial to ensure that the scope is set to the minimum necessary permissions to perform required tasks securely.
- **Avoid when:** The required permissions for the Pathlock platform to perform its tasks are not clear. Ensure to review and understand the access level provided by the scope setting to avoid providing overly broad access.