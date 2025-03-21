# Enable Automatic Approval

**Technical Name:** EnableAutomaticApproval

**Category:** Workflow

**Default Value:**

**Impact Level:**

**Description:**

The "Enable Automatic Approval" parameter is designed for use within the Pathlock Cloud GRC platform, specifically within the Workflow framework. This setting allows for the automatic approval of certain processes or actions without the need for manual intervention. This can streamline operations and enhance efficiency within an organization's governance, risk, and compliance (GRC) practices.

**Business Impact:**

Enabling this parameter can significantly impact the speed and efficiency of workflow approvals within an organization. It enables quicker decision making and reduces the workload on personnel who would otherwise need to manually approve each action. However, it also requires a high level of trust in the automated processes and the criteria set for auto-approval to ensure that only appropriate actions are approved without compromising security or compliance standards.

**Technical Impact: when configured**

Once configured, the "Enable Automatic Approval" parameter automates the approval process for transactions or activities within defined criteria. This means that any action falling within these predefined criteria will bypass the usual manual approval steps, being automatically approved by the system. 

**Examples Scenario:**

- **Streamlining Employee Onboarding:** In a scenario where an organization has a high volume of new hires, enabling automatic approval for certain onboarding steps can reduce the time spent on administrative processes, allowing new employees to become productive more quickly.

**Related Settings:**

- `GridEmployees.Columns`: Associated with the display and management of employee-related information within the workflow where automatic approvals might be applied.

**Best Practices:** 

- **Configure when**:
  - You have well-defined criteria that can be automated without compromising security or compliance.
  - There is a need to speed up repetitive approval processes that do not require detailed scrutiny.

- **Avoid when**:
  - The actions requiring approval involve significant security, compliance, or business impact risks.
  - Criteria for automatic approvals are not clear or are too broad, which could potentially automate decisions that should be reviewed manually.