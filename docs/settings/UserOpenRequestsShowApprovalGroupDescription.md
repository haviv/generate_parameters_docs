# User Open Requests Show Approval Group Description

**Technical Name:** UserOpenRequestsShowApprovalGroupDescription

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `UserOpenRequestsShowApprovalGroupDescription` parameter controls the visibility of approval group descriptions in the "My Requests" section of the Pathlock Cloud GRC platform. When enabled, users can view detailed descriptions of each approval group associated with their requests, providing clearer insight into the approval process.

**Business Impact:**

Enabling this feature enhances transparency for requestors by allowing them to understand the purpose and criteria of the approval groups handling their requests. This can lead to increased trust in the compliance process, as users have a better grasp of why certain requests are subject to specific approval workflows.

**Technical Impact when configured:**

Upon configuration, the user interface for open requests will include additional descriptive text for each approval group. This may slightly alter the layout or design of the "My Requests" section, depending on the length and formatting of the approval group descriptions.

**Examples Scenario:**

A user submits a request for elevated system access. With the `UserOpenRequestsShowApprovalGroupDescription` parameter enabled, the user can view a description of the approval group, such as "IT Security Approval - Handles requests for administrative access, ensuring compliance with IT security policies." This clarifies for the requestor why their request is directed to this particular group.

**Related Settings:**

- ShowCreatedOnColumn

**Best Practices:** 

- **Configure when:** There's a need for greater transparency in the approval process, and when descriptions can aid users in understanding the flow and rationale behind approval decisions.
- **Avoid when:** Approval group descriptions are overly lengthy, sensitive, or could confuse the process for users.