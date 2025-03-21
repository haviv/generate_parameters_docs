# New Direct Manager Template

**Technical Name:** NewDirectManagerTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The NewDirectManagerTemplateId parameter is used within the Pathlock Cloud GRC platform for facilitating the creation of new approval groups in workflows related to direct manager approvals. It specifically pertains to scenarios where a new group is generated as part of workflow steps that require manager approval.

**Business Impact:**

The configuration of this parameter impacts the efficiency and effectiveness of approval workflows within an organization's GRC processes. By facilitating the automatic creation of approval groups based on specific criteria, it enhances the operational efficiency of review and approval processes, ensuring that actions are appropriately authorized before proceeding.

**Technical Impact when configured:**

Configuring the NewDirectManagerTemplateId influences the workflow engine’s ability to automatically create and manage approval groups. This auto-generation supports the maintenance of a streamlined approval process by ensuring that appropriate managerial oversight is programmed into the workflow without manual intervention, thereby reducing the potential for delay or oversight.

**Examples Scenario:**

- **Scenario:** An organization requires that any access changes within its IT systems receive approval from an employee's direct manager. When a change request is initiated, the NewDirectManagerTemplateId parameter ensures that an approval group containing the direct manager is automatically created and assigned to the approval step if not already present.
  
**Related Settings:**

- `UpdateCachePeriodForAprpovalGroups`: Determines the frequency (in minutes) at which the approval groups cache is updated, which could indirectly affect how quickly new direct manager approval groups are recognized by the system.

**Best Practices:** 

- **Configure when:** Setting up or revising workflows that involve manager approvals to ensure efficiency in group creation and assignment.
- **Avoid when:** Direct manager approvals are not a part of your organization’s workflow processes, or when manual group assignment is preferred for greater control.
