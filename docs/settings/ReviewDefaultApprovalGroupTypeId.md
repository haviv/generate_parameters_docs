# Review Default Approval Group Type

**Technical Name:** ReviewDefaultApprovalGroupTypeId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** The `ReviewDefaultApprovalGroupTypeId` parameter specifies the default type of approval group used during the review processes within Pathlock Cloud GRC platform workflows. It determines the grouping criteria for approval processes, ensuring that review actions are routed to the appropriate group based on predefined conditions.

**Business Impact:** Proper configuration of this parameter ensures that workflow review processes are streamlined and that approval requests are automatically sent to the correct group. This can significantly impact the efficiency of review and approval processes within the organization, directly affecting compliance management and operational efficiency.

**Technical Impact when configured:** Configuring this parameter influences how the system identifies and assigns approval requests. A correctly set default approval group type ensures operational workflows are consistent with the organizational structure and governance policies, leading to improved risk management and compliance adherence.

**Examples Scenario:** If an organization has multiple departments with varying levels of authority for approval, the `ReviewDefaultApprovalGroupTypeId` can be set to route financial approvals to the finance department and IT-related approvals to the IT department's approval group.

**Related Settings:**

- `CommonSettings.Default.LoginMethod`: Ensures that user authentication methods are considered when routing approval requests within the specified default approval group type.

**Best Practices:** 

- **Configure when:** Establishing or updating workflows that require distinct approval processes across different departments or teams within the organization.
  
- **Avoid when:** If the organization has a flat approval structure or does not require specific groups for different types of approval processes, unnecessary configuration of this parameter may complicate the workflow unnecessarily.