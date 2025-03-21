# Mitigate Violation Show Approve Reason Only

**Technical Name:** MitigateViolation_ShowApproveReasonOnly

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The MitigateViolation_ShowApproveReasonOnly parameter controls whether users are required to provide a reason for approving a mitigation action for a violation in the Pathlock Cloud GRC platform. When set to True, it restricts the interface to only show the approval reason input, simplifying the user experience and focusing on the rationale behind the mitigation approval.

**Business Impact:**

Enabling this parameter ensures that mitigation approvers provide a reason for their decisions, enhancing audit trails and accountability within the organization's GRC processes. This can lead to more informed decision-making and improved compliance posture by emphasizing the justification for mitigations.

**Technical Impact when configured:**

When configured to True, the user interface for mitigating violations is streamlined to only include the approval reason field, thereby enforcing a mandatory input of approval reasoning by the approver. This can impact workflows by focusing attention on the justification for approval, potentially improving the quality of audit information.

**Examples Scenario:**

- A user is mitigating a violation related to a segregation of duties (SOD) conflict. With the MitigateViolation_ShowApproveReasonOnly parameter set to True, the system prompts the user to enter a reason for approving the mitigation without displaying additional/irrelevant options.
  
- During audit reviews, auditors can easily identify why each mitigation was approved, as each approval includes a mandatory reason, streamlining the audit process.

**Related Settings:** 

MitigateViolation_ShowApproveReasonAndControl (considering the similar naming convention and the consistent context of mitigation approval process).

**Best Practices:** 

- **Configure when:** You want to ensure that each mitigation approval within your GRC processes is accompanied by a reason, enhancing accountability and traceability.
  
- **Avoid when:** The requirement for an approval reason may slow down the mitigation process or if the rationale behind mitigation approvals is managed outside the Pathlock platform.