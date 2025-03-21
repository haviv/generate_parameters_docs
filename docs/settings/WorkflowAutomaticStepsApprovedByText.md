**Workflow Automatic Steps Approved By Text**

**Technical Name:** WorkflowAutomaticStepsApprovedByText

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `WorkflowAutomaticStepsApprovedByText` parameter is used in the Pathlock Cloud GRC platform to designate a placeholder or identifier for the automated approval process within various workflow elements. It serves as a means to identify or tag steps that have been approved automatically, without direct human intervention, in the workflow process.

**Business Impact:**

The automation of step approvals through this parameter can significantly streamline the workflow processes by reducing the manual overhead required for approval steps. It ensures timely execution of the workflows, which is vital in managing security, risk, and compliance (GRC) more efficiently within an organization. It directly impacts the speed and efficiency of GRC-related workflows, such as Authorization Certification, and indirectly supports compliance by ensuring necessary steps are approved within the required timelines.

**Technical Impact when configured:**

- Enhances workflow automation by providing a means to recognize and handle automatically approved steps.
- Facilitates easier tracking and auditing of automated approvals within the workflow process.
- Can reduce the potential for human error by minimizing the need for manual step approvals.

**Examples Scenario:**

In a situation where an organization needs to conduct a User Access Review (UAR) or Segregation of Duties (SOD) campaign, the WorkflowAutomaticStepsApprovedByText parameter could be used to automate approvals for steps that do not require detailed scrutiny or have been pre-validated through other means. This ensures that the focus is maintained on critical review steps that require attention, thereby optimizing the overall process.

**Related Settings:**

- CommonSettings.Default.SinglePageReview
- ReviewElement.MonitoredRuleException
- ReviewElement

**Applicable Workflows Actions:** 

- AuthoirizationCertificationBO
- ApproveStep
- ForwardToNextStepOnSpecificDate

**Best Practices:** 

- **configure when:** you have workflow steps that are routine and can be approved based on predefined criteria without human intervention.
- **avoid when:** the step requires detailed review or when automated approval may bypass critical compliance checks.