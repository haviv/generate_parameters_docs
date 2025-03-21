# Disable Approval Check By Request Submitter

**Technical Name:** DisableApprovalCheckByRequestSubmitter

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the system should bypass the approval check for actions requested by the same user who is designated as the approver. When enabled, it removes the necessity for request submitters to approve their own requests, streamlining workflows where users have dual roles.

**Business Impact:**

Enabling this setting can significantly reduce the administrative overhead in processes where users often initiate requests requiring their own approval. It accelerates the execution of workflows by removing redundant steps, which is crucial in fast-paced environments. However, it should be used cautiously as it impacts the segregation of duties principles by allowing actions without independent approval.

**Technical Impact when configured:**

When set to true, the system will not prevent a user from approving their own requests. This might be desirable in scenarios where the user's role encompasses both requesting and approving specific actions, eliminating potential bottlenecks in the workflow process.

**Examples Scenario:**

A user in a managerial position needs to request access to a sensitive system for a project. In this scenario, the manager is also the approver for such requests. With this configuration set to true, they can submit and approve the request without needing another party to intervene, expediting access and project commencement.

**Related Settings:**

None specifically related were identified in the provided code references.

**Best Practices:** Configure when the workflow process can be reliably expedited by allowing self-approvals, ensuring that the risk exposure is acceptable. Avoid when strict compliance with segregation of duties is required, or if the potential for abuse by bypassing independent approval checks is high.