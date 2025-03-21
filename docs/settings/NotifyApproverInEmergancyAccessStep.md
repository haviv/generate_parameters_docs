# Notify Approver In Emergency Access Step

**Technical Name:** NotifyApproverInEmergancyAccessStep

**Category:** Workflow

**Default Value:** (Not provided in code references)

**Impact Level:** High

**Description:**

This parameter controls whether approvers are notified during the Emergency Access step in Pathlock's cloud GRC platform workflows. When enabled, approvers will be alerted immediately if a step precedes an approval action within an emergency access workflow, ensuring that critical access requests are addressed promptly and efficiently.

**Business Impact:**

Enabling this parameter ensures that key personnel are swiftly notified in situations requiring emergency access, minimizing delays in response times and reducing the risk to business operations from unaddressed access requests.

**Technical Impact when configured:**

When enabled, the system initiates a notification process for approvers ahead of emergency access steps if the preceding steps are configured with approval requirements. This setup is crucial in time-sensitive situations or during incidents where immediate action is required, ensuring that all relevant parties are informed and able to take necessary action without delay.

**Examples Scenario:**

Imagine a scenario where an employee requires emergency access to a critical system following the sudden unavailability of a key staff member. By having the NotifyApproverInEmergancyAccessStep parameter enabled, the workflow automatically notifies approvers about the urgent access request, facilitating a faster approval process and ensuring that business continuity is maintained.

**Related Settings:** 

- `AuthorizationReviewShowStepNameColumnOnWaitingPage`
- `AuthorizationReviewShowHighRiskColumnOnDetailsPage`

**Best Practices:** 

- **Configure when:** Immediate notification of approvers is crucial for managing emergency access requests efficiently.
- **Avoid when:** If non-emergency workflows are predominantly used and immediate notification could lead to unnecessary alerts or interruptions.