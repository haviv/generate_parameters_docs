# Enable Smart Authorization Review

**Technical Name:** EnableSmartAuthorizationReview

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** High

**Description:**

Enables a smarter, more efficient review process by focusing on partially reviewed authorizations, streamlining the authorization certification workflow. This ensures that attention is directed towards entries that require further action, improving the efficacy of the review process.

**Business Impact:**

Improving the authorization review process by ensuring a more targeted, efficient approach reduces the time and resources required for compliance activities. This leads to a more focused review process, potentially minimizing risks associated with overlooked authorizations and enhancing overall compliance posture.

**Technical Impact when configured:**

When this parameter is enabled, the system prioritizes users and their associated authorization steps that have been partially reviewed over those fully reviewed or not reviewed at all. This filtration facilitates focusing on areas that demand action, streamlining the overall review process and contributing to more efficient resource utilization and compliance management.

**Example Scenario:**

Consider an organization undergoing its periodic compliance checks, facing hundreds of user authorizations needing reviews. By enabling Smart Authorization Review, the system highlights only those users with partially reviewed statuses. This means reviewers can focus their efforts where it's most needed, ensuring a more efficient use of time and quicker compliance with regulatory requirements.

**Related Settings:** Not provided

**Applicable Workflows Actions:** Not provided

**Best Practices:** 

- **Configure when:** embarking on large-scale authorization review processes or when the existing process is noted to be inefficient or overly time-consuming.
  
- **Avoid when:** all authorizations require a full, comprehensive review every time, regardless of previous review status or where the organizational policy dictates that each authorization must be treated equally without prioritization.