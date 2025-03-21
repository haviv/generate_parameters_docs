# Authorization Review In Requests Waiting Page

**Technical Name:** AuthorizationReviewInRequestsWaitingPage

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The 'AuthorizationReviewInRequestsWaitingPage' parameter controls the visibility and behavior of authorization reviews in the requests waiting for approval page within the Pathlock Cloud GRC platform. Specifically, it manages aspects such as whether mass approval pop-ups are shown, and the display of certain buttons related to the authorization process.

**Business Impact:**

Configuring this parameter properly ensures that the approval process is streamlined and efficient, by either simplifying the user interface for approvers or providing them with the necessary tools for bulk actions. Incorrect configurations can lead to unnecessary complexity in approval processes or potentially overlooked authorization requests, impacting the timely execution of security, compliance, and risk management processes.

**Technical Impact when configured:**

- Disabling mass approval pop-ups can speed up the approval process for users who are reviewing a small number of requests.
- Hiding or showing specific controls based on this parameter can tailor the user experience to the needs of the organization, making the workflow more intuitive.
- Adjustments to this parameter can affect how approvers interact with the approval queue, potentially leading to faster or more secure approval cycles based on the visibility of certain buttons and options.

**Examples Scenario:**

Imagine an organization undergoing an audit requiring detailed review of all authorization requests. The 'AuthorizationReviewInRequestsWaitingPage' parameter could be configured to show all options for detailed review, including the display of mass approval pop-ups, ensuring that each request is intentionally reviewed and approved or declined, aiding in meeting stringent compliance requirements.

**Related Settings:**

**Best Practices:** configure when you need to streamline the approval process by removing unnecessary options or to enforce a more detailed review process for certain types of requests. Avoid configurations that could lead to oversight of critical authorization requests or unnecessarily slow down the approval process for routine requests.