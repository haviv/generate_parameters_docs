# Impact Analysis Show Risk Level

**Technical Name:** ImpactAnalysisShowRiskLevel

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The ImpactAnalysisShowRiskLevel parameter controls whether the risk level is visible during the workflow process for role creation and modification within the Pathlock Cloud GRC platform. This setting influences how risk is communicated and addressed during the approval stages of workflow processes, especially in scenarios related to role management.

**Business Impact:**

Enabling this parameter ensures that decision-makers have clear visibility of the risk level associated with creating or modifying roles, aiding in making more informed decisions that align with the organization's risk management strategy.

**Technical Impact when configured:**

When configured, this parameter adds an additional layer of risk visibility to the workflow process. It facilitates risk-informed decisions by highlighting the risk level directly within the workflow interface, allowing approvers to assess risk implications more effectively.

**Examples Scenario:**

- **Role Creation:** When a new role is requested through the workflow, enabling this parameter would display the associated risk level of assigning certain permissions, helping to prevent overly permissive roles from being created without due consideration of the associated risks.
  
- **Role Modification:** Before approving modifications to an existing role, the displayed risk level helps in assessing the security implications of the proposed changes.

**Related Settings:**

- WorkflowCommentsButtonTextOverride

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when** initiating any role creation or modification workflows to enhance risk visibility and governance.
  
- **Avoid when** the decision-making process is streamlined and does not require risk level assessment visibility to fast-track role adjustments.
