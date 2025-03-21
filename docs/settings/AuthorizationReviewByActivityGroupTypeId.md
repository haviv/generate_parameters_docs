# Authorization Review By Activity Group Type

**Technical Name:** AuthorizationReviewByActivityGroupTypeId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to control the behaviors of authorization reviews within the Pathlock Cloud GRC platform. When enabled, it allows for the examination of user permissions by grouping activities, possibly streamlining the review process for complex authorization scenarios.

**Business Impact:**

Enabling reviews by activity group type can significantly impact how efficiently an organization can conduct compliance and risk assessment activities related to user permissions. It facilitates more granular control and visibility over the authorization process, potentially reducing the risk of unauthorized access and ensuring compliance with relevant regulations and standards.

**Technical Impact when configured:**

Upon configuration, this setting customizes the authorization review process to focus on specific activity groups. This means that reviews could be more targeted, focusing on high-risk or critical activity groups first, or tailored based on the organization's specific compliance needs.

**Example Scenario:**

A financial organization needs to ensure that only authorized personnel have access to sensitive transaction processing systems. By utilizing the AuthorizationReviewByActivityGroupTypeId, they can group transaction-related activities together and conduct focused reviews on these groups, identifying any discrepancies or unauthorized access more efficiently.

**Related Settings:**

- AuthorizationRequestAdditionalNumberOfMultipleRows

**Best Practices:** 

- **Configure when:** You have a complex set of permissions and activity types within your organization, and there's a need to tailor the authorization review process to specific groups of activities for better manageability and oversight.
  
- **Avoid when:** Your organization's authorization structures are straightforward or if grouping activities might lead to overlooking specific, less prominent permissions that also require review.