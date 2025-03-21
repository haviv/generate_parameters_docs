# Role Builder Workflow Type

**Technical Name:** RoleBuilder_WorkflowTypeId

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

The Role Builder Workflow Type parameter is designed to identify and manage the types of workflows associated with role creation and modification processes within the Pathlock Cloud GRC platform. It plays a critical role in streamlining role management, ensuring compliance, and enhancing the security posture by enabling automated workflows for role-related tasks.

**Business Impact:**

Setting this parameter correctly ensures that role management processes are aligned with organizational policies and compliance requirements. It reduces the risk of unauthorized access or privilege escalation by enforcing proper workflow steps for role creation and modifications, thereby maintaining a strong security framework within the organization.

**Technical Impact when configured:**

When the RoleBuilder_WorkflowTypeId is configured, it directly impacts how roles are created, modified, and managed within the system. It dictates the flow of tasks and approvals required, ensuring that all changes are tracked and audited. This leads to a more controlled and secure role management process, mitigating risks associated with manual interventions and errors.

**Example Scenario:**

For instance, in an organization where separation of duties (SOD) is crucial, configuring this parameter to include approval workflows for role changes can help prevent conflicts of interest by ensuring that changes to roles are reviewed and approved by multiple stakeholders. This can aid in compliance with regulatory standards like SOX or GDPR which require stringent controls over access to sensitive information.

**Related Settings:**

- `ProcessFailedToStartForSystem`
- `RiskChartDataNumberOfMonths`

**Best Practices:** 

- **Configure when:** setting up role management processes within Pathlock to ensure automated, compliant, and secure workflows.
  
- **Avoid when:** the exact requirements for role management workflows are unclear, as incorrect configuration can lead to workflow errors or security loopholes. It is best to understand the organization's role management needs and security policies thoroughly before setting this parameter.