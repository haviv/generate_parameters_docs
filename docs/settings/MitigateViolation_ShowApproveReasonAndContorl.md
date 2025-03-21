**Mitigate Violation Show Approve Reason And Control**

**Technical Name:** MitigateViolation_ShowApproveReasonAndContorl

**Category:** Compliance

**Default Value:** 

**Impact Level:** Medium

**Description:**

This configuration parameter controls the visibility and requirement for entering a reason and related control information when mitigating a violation in the Pathlock Cloud GRC platform. It ensures that users provide a justification and reference the control mechanism applied as part of the mitigation process.

**Business Impact:**

Enabling this parameter reinforces accountability and transparency within the organization's compliance and risk management processes. It ensures that every mitigation action is justified and linked to a control, facilitating audits and compliance reviews.

**Technical Impact when configured:**

When enabled, users must provide a reason and select a control measure while mitigating a violation. This enhances the quality of the mitigation process and improves the documentation for compliance and audit purposes.

**Examples Scenario:**

- An unauthorized access violation is identified in the system. To mitigate this violation, the responsible manager must specify the reason for the access and link the mitigation to a specific internal control, such as revised access control procedures or user access review processes.

**Related Settings:**

- AutomaticWorkflowSoDMitigatedPeriodInDays

**Best Practices:** configure when any mitigation action requires explicit documentation of the reason and the control applied. Avoid when the organization's process is less formal and does not require stringent documentation for violations mitigation.