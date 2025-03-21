# Workflow Details Screen Tabs View

**Technical Name:** WorkflowDetailsScreenTabsView

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `WorkflowDetailsScreenTabsView` parameter controls how additional components or tabs related to workflow steps are displayed within the Pathlock Cloud GRC platform's workflow details screen. It is designed to enhance the usability and visualization of workflow-related information for end users, facilitating a smoother navigation experience through the various workflow steps and their details.

**Business Impact:**

Effective use of the `WorkflowDetailsScreenTabsView` parameter can significantly improve the efficiency of auditing and managing workflows by providing a clearer, more organized view of the workflow steps and relevant details. This can lead to improved compliance and risk management, as users are better equipped to review and make decisions based on the presented information.

**Technical Impact when configured:**

When properly configured, the parameter can alter the default presentation of the workflow details screen, potentially grouping certain information into tabs or dropdown menus based on the workflow step context. This customization allows for a more streamlined, focused interaction with the platform, reducing cognitive load and enhancing the decision-making process within GRC functions.

**Examples Scenario:**

- **Enhancing Workflow Visualization:** In a scenario where an organization has complex workflows with multiple steps requiring review and approval, the `WorkflowDetailsScreenTabsView` parameter can be configured to display specific tabs for attachments, roles, and free-text inputs. This organization allows users to quickly access pertinent information, making the review process more efficient.

**Related Settings:**

- `TakeOnlyRolesFromCurrentSystem`: Filters roles presented in a workflow step to those relevant to the current user's system, enhancing relevance and focus.

**Best Practices:** 

- **Configure when:** There is a need to simplify the workflow details view for end users, especially in complex workflows with multiple steps and associated information.
- **Avoid when:** The default workflow details presentation meets the organization's needs for simplicity and clarity, or when changes might confuse users accustomed to the standard layout.