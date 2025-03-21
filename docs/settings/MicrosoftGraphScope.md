**Microsoft Graph Scope**

**Category:** Configuration

**Default Value:** `null`

**Impact Level:** Medium

**Description:**

The Microsoft Graph Scope parameter is used to configure the level of access required by the Pathlock Cloud GRC platform when interacting with Microsoft Graph API. It determines what resources and operations the application can perform on behalf of the user within Microsoft services.

**Business Impact:**

Proper configuration of the Microsoft Graph Scope is crucial for enabling seamless and secure integration with Microsoft services such as Office 365, ensuring that Pathlock Cloud GRC platform has the necessary permissions to perform its tasks without exceeding the intended level of access, enhancing both security and functionality.

**Technical Impact when configured:**

When properly configured, the Microsoft Graph Scope ensures that the Pathlock Cloud GRC can efficiently manage security, compliance, and risk management tasks related to Microsoft services by accessing specific Microsoft Graph API resources. A misconfiguration could lead to inadequate access levels, impacting the platform's functionality or compromising security.

**Example Scenario:**

Imagine a scenario where the Pathlock Cloud GRC platform needs access to read emails from Office 365 for compliance auditing purposes. By configuring the Microsoft Graph Scope to include Mail.Read permissions, the platform can perform this task efficiently without requiring full access to the user's Office 365 account, adhering to the principle of least privilege.

**Related Settings:**

- `WorkflowAuthorizationReviewReminderContainer`
- `WorkflowAutomaticStepsApprovedByText`
- `WorkflowDeclined`
- `WorkflowReminderAuthorizationCertificationFormat`

**Best Practices:** 

- **Configure when:** You need to integrate Pathlock Cloud GRC platform functionalities with Microsoft services, ensuring you only request the necessary permissions to perform required tasks.
- **Avoid when:** If there is no clear requirement or understanding of the permissions needed, as improper scope could lead to security risks or functional limitations.