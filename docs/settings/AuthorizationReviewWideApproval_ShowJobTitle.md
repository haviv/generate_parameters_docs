**Authorization Review Wide Approval Show Job Title**

**Technical Name:** AuthorizationReviewWideApproval_ShowJobTitle

**Category:** Workflow

**Default Value:** (No default value was specified in the provided code references)

**Impact Level:** Medium

**Description:**

The AuthorizationReviewWideApproval_ShowJobTitle parameter controls whether job titles should be displayed alongside user names during the authorization review process in wide approval scenarios within the Pathlock Cloud GRC platform. This setting enhances clarity and context during review processes by associating users with their respective roles within the organization.

**Business Impact:**

Including job titles in the review process provides reviewers with additional context, potentially enabling more informed decision-making. This detail could be particularly significant in large organizations where reviewers might not be personally familiar with each individual requiring authorization, thereby improving the accuracy and efficiency of reviews.

**Technical Impact when configured:**

When configured to show job titles, the display of employee information within the authorization certification workflow is augmented to include each user's job title alongside their name. This change applies to scenes such as waiting for approvals in the ProfileTailorApp, affecting both version 1 and version 2 of the waiting pages (WaitingV1.aspx.cs and WaitingV2.aspx.cs). 

**Example Scenario:**

In a scenario where an organization is undergoing a monthly review of user access rights, the Authorization Review Wide Approval Show Job Title parameter can help reviewers quickly identify and verify the appropriateness of access levels based on employees' job titles. For instance, if a user with a job title indicating a finance department role is requesting access to a sensitive HR system, this may prompt additional scrutiny or discussion.

**Related Settings:**

No directly related settings were identified in the provided code references.

**Best Practices:** 

- **Configure when:** You are operating in an environment where reviewers benefit from additional context about the individuals whose authorizations they are reviewing. This is especially relevant in large or complex organizational structures where job roles are critical for access decisions.
- **Avoid when:** Displaying job titles might breach privacy policies, or where job titles could lead to biased decision-making during the review process.