# Review Authorizations Show Employee

**Technical Name:** ReviewAuthorizationsShowEmployee

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the display of employee data within the Review Authorizations process in the Pathlock Cloud GRC platform, specifically during the execution of the `AuthoirizationCertificationBO` workflow action. When enabled, it ensures that employee-related information is visible, providing a comprehensive view of the authorization data being reviewed.

**Business Impact:**

Enabling this setting enhances the transparency and traceability of authorization reviews by providing a complete overview of the employees involved. This facilitates more informed decision-making by reviewers, contributing to improved internal controls and compliance management.

**Technical Impact when configured:**

Upon configuration, this parameter affects the display of progress data involving employee actions and authorizations, ensuring that summaries of authorization certification processes include relevant employee information. This can help to streamline the review process by making it easier for reviewers to correlate authorization actions with specific employees.

**Example Scenario:**

In a scenario where an organization is conducting a quarterly review of its internal access controls and authorizations, enabling the `ReviewAuthorizationsShowEmployee` parameter allows reviewers to see not only which authorizations are being reviewed but also which employees are affected by these authorizations. This level of detail is crucial for audits and compliance checks, ensuring that any access-related risks are appropriately managed and mitigated.

**Related Settings:**

- CampaignProgressBarRoundPercentage

**Applicable Workflows Actions:**

- AuthoirizationCertificationBO

**Best Practices:** configure when conducting detailed authorization reviews or audits that require visibility of employee-specific information; avoid when unnecessary to minimize information overload during the review process.