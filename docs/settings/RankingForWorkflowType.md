# Ranking For Workflow Type

**Technical Name:** RankingForWorkflowType

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** 

The `RankingForWorkflowType` parameter is used within the Pathlock Cloud GRC platform to prioritize or rank workflow instances based on their types. This parameter comes into play when sorting or filtering workflows, allowing for a customized approach to handle business processes within an organization. 

**Business Impact:**

The proper configuration of this parameter directly affects how efficiently workflow instances are processed and addressed. For organizations with a multitude of workflows, setting an appropriate ranking ensures that critical or high-priority workflows are attended to promptly, impacting compliance, operational efficiency, and risk management processes.

**Technical Impact when configured:**

When `RankingForWorkflowType` is configured, it alters the default processing order of workflow instances within the Pathlock Cloud GRC platform. This can lead to an optimized workflow handling process by ensuring that higher-ranked workflow types are presented or processed before others according to business needs.

**Examples Scenario:**

- **Prioritizing Compliance Over Onboarding:** An organization might configure `RankingForWorkflowType` to prioritize compliance-related workflows over employee onboarding workflows. This ensures critical compliance tasks are completed in a timely manner, reducing risk.

**Related Settings:**

- `WorkflowInstanceId`
- `BusinessRoleId`
- `OrgUnits`

**Best Practices:** configure when you need to emphasize certain workflows within your organizational processes to ensure they are handled with the priority they require. Avoid overcomplicating the configuration to prevent unnecessary administrative overhead and confusion.