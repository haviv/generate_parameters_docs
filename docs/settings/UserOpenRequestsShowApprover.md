# User Open Requests Show Approver

**Technical Name:** UserOpenRequestsShowApprover

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

The UserOpenRequestsShowApprover parameter determines whether or not the approver's information is displayed to the end-user within various workflow interfaces where user requests are listed. This includes pages that show open requests, requests awaiting approval, and request histories.

**Business Impact:**

Enabling this option enhances transparency within the user request process by allowing employees to see who is responsible for approving their requests. This visibility can improve communication and efficiency by potentially reducing follow-up inquiries to administrative or IT departments regarding request statuses.

**Technical Impact when configured:**

- If set to `True`, the approver's information will be shown alongside each request in the user's view.
- If set to `False`, this information is hidden, simplifying the display but reducing transparency.

**Examples Scenario:**

- An employee submits a request for access to a particular system. With `UserOpenRequestsShowApprover` enabled, the employee can see who the approver is for their request and may choose to follow up directly with them if there’s a delay or a need for clarification.
- In a scenario where minimizing distraction and information overload is paramount, setting this parameter to `False` might be preferable, especially in environments with a straightforward approval process or where approvals are managed centrally.

**Related Settings:**

- `UserOpenRequestsShowEndLink`

**Best Practices:** 

- Configure when:
  - Transparency in the approval process is essential.
  - Users benefit from knowing who their approvers are to manage communications more effectively.
  
- Avoid when:
  - The approval process is intended to be abstracted from the end user.
  - It's necessary to streamline the user interface by hiding non-essential information.