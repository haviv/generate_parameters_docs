# Authorization Certification Show User Review In Wide Approval Screen

**Technical Name:** AuthorizationCertificationShowUserReviewInWideApprovalScreen

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter decides if user reviews for authorization certifications should be displayed in a wide format on the approval screen. This enhances clarity and usability by providing more space for information, facilitating better decision-making.

**Business Impact:**

When enabled, this configuration can significantly improve the user experience during the review and approval process of authorizations by providing a comprehensive view of user roles and permissions. This ensures that approvers have all necessary information available in an accessible format, mitigating the risk of oversight during certification.

**Technical Impact when configured:**

- The approval screen's layout will alter to accommodate a wider view of user reviews.
- Potentially increases the efficiency of the review process due to better visibility of user details.
- Helps in reducing the errors or misinterpretations that might happen due to cramped information presentation.

**Examples Scenario:**

- A Compliance Officer needs to review several user roles and permissions assignments as part of the quarterly audit process. Enabling this parameter will display all necessary information in a wider view, making it easier to assess compliance and identify any discrepancies without having to navigate through cramped data presentations.

**Related Settings:**

- WorkflowLocalizationByFieldId

**Best Practices:** configure when the default screen size does not suffice to clearly display all necessary information for a thorough review. Avoid when the additional space is not needed or could overwhelm the approvers with too much information at once.