# Request Details Redirect To Referrer

**Technical Name:** RequestDetailsRedirectToReferrer

**Category:** Workflow

**Default Value:** "~/Workflow/RequestsWaitingForApproval.aspx"

**Impact Level:** Medium

**Description:**

This parameter controls the redirection behavior for users after they interact with a request detail. Instead of navigating to a static page after performing an action, users are redirected back to a referring page, typically enhancing usability and workflow efficiency.

**Business Impact:**

Improves user experience by reducing the number of clicks and navigation steps required to return to relevant pending actions or information. This can lead to increased productivity and faster decision-making within the GRC processes.

**Technical Impact when configured:**

When configured, users are redirected to a more contextually relevant page (usually the list of requests waiting for approval) after performing an action in the request details page. This setup can significantly streamline workflows, particularly in environments with high volumes of requests.

**Examples Scenario:**

A user reviews a compliance request in detail and decides to approve it. Instead of being redirected to a generic dashboard or homepage, the user is taken back to the list of "Requests Waiting For Approval," where they can continue their work, reviewing and approving more requests without unnecessary navigation.

**Related Settings:**

- RequestDetailsRedirectToUrl

**Best Practices:** configure when workflows require fast-paced decision-making and frequent interaction with request details, avoid when users need to perform detailed analysis or follow-up actions that do not relate to the request approval process directly after interacting with a request.