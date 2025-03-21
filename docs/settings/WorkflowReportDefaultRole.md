# Workflow Report Default Role

**Technical Name:** WorkflowReportDefaultRole

**Category:** Reporting

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** This parameter is crucial for customizing how reports are managed and displayed within the Pathlock Cloud GRC platform, particularly regarding workflow processes.

**Business Impact:** Proper configuration of this parameter ensures that reports related to workflow processes are accessible by appropriate roles within the organization. It directly influences the efficiency of workflow management, decision-making processes, and compliance adherence by ensuring the right personnel have access to necessary reports.

**Technical Impact when configured:** Defines the default role that has the ability to view and manage workflow reports. Misconfiguration may lead to unauthorized access or, conversely, restrict necessary access to critical workflow information, impacting process optimization and compliance tracking.

**Examples Scenario:** If the Workflow Report Default Role is set to 'Workflow Manager', only users assigned this role can view and manage workflow-related reports. This ensures that sensitive information is guarded and that workflow management is streamlined and efficient.

**Related Settings:** 

- `CustomRolesThatAllowWorkflowManager`: This setting defines which custom roles are granted permissions similar to the 'Workflow Manager,' indicating a possible relation in controlling access rights within workflows and related reports.

**Best Practices:** 

- Configure this parameter at the initial setup of the Pathlock platform to align with your organization's policy on role-based access control.
  
- Avoid configuring this parameter without a clear understanding of the organizational roles and permissions structure to prevent unauthorized access or unnecessary restrictions on workflow reports.