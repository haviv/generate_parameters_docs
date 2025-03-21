# Show Is Approved Dialog

**Technical Name:** ShowIsApprovedDialog

**Category:** Workflow UI

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Show Is Approved Dialog parameter controls whether or not a confirmation dialog appears in the user interface after an approval action is completed within a workflow. This parameter ensures users receive immediate feedback on the outcome of their actions, enhancing user experience and reducing the need for additional checks to confirm approval status.

**Business Impact:**

Implementing the Show Is Approved Dialog feature significantly impacts operational efficiency by confirming that approval actions have been successfully processed. This clarity leads to better decision-making and can reduce the administrative burden on teams verifying approval statuses, thus ensuring smoother workflow transitions and adherence to compliance and policy requirements.

**Technical Impact when configured:**

When enabled, this setting initiates a user interface prompt confirming that an approval has been successfully registered in the system. It reassures users that their action has taken the intended effect, eliminating uncertainty and the potential for error due to unacknowledged approvals.

**Examples Scenario:**

A user completes an approval action for a critical compliance document within the Pathlock GRC platform. Upon submission, if the Show Is Approved Dialog feature is enabled, a confirmation dialog box will appear, indicating that the document has been successfully approved. This immediate feedback allows the user to proceed confidently without needing to double-check the approval status.

**Related Settings:** 

- AuthorizationReviewLinkToPortalVisible
- AuthorizationReviewLinkToPortalText

**Best Practices:** 

- **Configure when:** Immediate user feedback on approval actions is crucial, especially in complex workflows where each step's completion is critical for compliance and audit trails.
- **Avoid when:** The additional confirmation step might interrupt or slow down the workflow for experienced users who prefer a streamlined process without additional confirmations.