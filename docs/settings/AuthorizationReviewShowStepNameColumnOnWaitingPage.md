# Authorization Review Show Step Name Column On Waiting Page

**Technical Name:** AuthorizationReviewShowStepNameColumnOnWaitingPage

**Category:** Authorization Review

**Default Value:**

**Impact Level:**

**Description:**
This setting controls the visibility of the 'Step Name' column on the waiting page during the Authorization Review process in the Pathlock Cloud GRC platform. When enabled, it adds a column that displays the name of each step in the review process, providing users with clearer context and understanding of the stage at which each authorization request is currently pending.

**Business Impact:**
Enabling this feature can significantly enhance the review process by improving transparency and communication between approvers and requesters. By clearly seeing the step name associated with each authorization request, approvers can prioritize their work more effectively, potentially leading to faster approval times and reduced bottlenecks in the review process. This setting is crucial for organizations that manage a high volume of authorization requests and strive for efficient governance, risk, and compliance (GRC) practices.

**Technical Impact: when configured**
Upon configuration, the system will dynamically add the 'Step Name' column to the waiting page within the Authorization Review module. This does not affect the underlying data or the review process itself but modifies the user interface to include additional, informative content that aids in the review process.

**Examples Scenario:**
- A company conducts regular Authorization Reviews as part of its compliance requirements. By enabling this feature, each request on the waiting page will explicitly show at what step of the review process it is. This clarity helps in identifying bottlenecks where requests are piling up, allowing for targeted action to improve flow and efficiency.
  
- During peak operation times, an organization finds that certain steps in the authorization process are prone to delays. By displaying the step name prominently, process managers can quickly allocate more resources or apply additional scrutiny to steps that are identified as problematic, directly from the waiting page.

**Related Settings:**
- AuthorizationReviewShowHighRiskColumnOnDetailsPage
- AuthorizationReviewShowPartialApprovalIcon
- AuthorizationReviewShowPartialApprovalText

**Best Practices:** 
- **Configure when:** There is a need to improve the transparency and traceability of the Authorization Review process, especially in complex workflows or high-volume environments.
- **Avoid when:** The additional information might overwhelm the users or when the review process is straightforward and does not benefit from the added visibility of step names.