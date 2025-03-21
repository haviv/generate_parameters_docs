# Authorization Review Show High Risk Column On Details Page

**Technical Name:** AuthorizationReviewShowHighRiskColumnOnDetailsPage

**Category:** Authorization Review

**Default Value:**

**Impact Level:** High

**Description:**

Enables the display of a dedicated column to highlight high-risk permissions or roles directly on the authorization review details page. This setting aims to facilitate immediate recognition of areas requiring urgent attention by compliance and security teams during the certification process.

**Business Impact:**

By activating this feature, organizations can enhance their risk management practices by ensuring that high-risk permissions are prominently highlighted during the review process. This aids in the prioritization of security concerns and supports a proactive approach to mitigating potential compliance issues.

**Technical Impact when configured:**

When enabled, the user interface for authorization reviews will include an additional column specifically designated for identifying high-risk items. This adjustment enables reviewers to quickly assess the risk level of permissions or roles without needing to navigate away from the details page. 

**Examples Scenario:**

A financial institution uses this parameter to streamline their quarterly access reviews by immediately flagging roles that have transactional capabilities exceeding a predefined threshold, allowing reviewers to focus on these roles for detailed evaluation.

**Related Settings:**

- MaxReplaceTemplateValusCounter
- ReplaceTemplateForWorkflowParameter

**Best Practices:** configure when you need to streamline the review process by immediately identifying high-risk permissions or roles. Avoid when unnecessary to reduce information overload on the details page.