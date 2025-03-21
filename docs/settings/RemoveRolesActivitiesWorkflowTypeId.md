# Workflow Type to Remove Activities from Role

**Technical Name:** RemoveRolesActivitiesWorkflowTypeId

**Category:** Workflow

**Default Value:** -1

**Impact Level:** High

**Description:** Identifies the specific type of workflow designed to handle the removal of activities from roles within the Pathlock Cloud GRC platform.

**Business Impact:** Ensuring that roles are appropriately managed by removing outdated or unnecessary activities is crucial for maintaining the integrity of access controls and compliance within an organization. This parameter aids in automating the process, thereby reducing the risk of manual errors and enhancing the overall security posture.

**Technical Impact when configured:** When configured with a valid workflow type ID, this setting triggers the specified workflow to process the removal of activities from roles. This automated workflow helps streamline the modification of roles, ensuring that changes are made consistently and are in compliance with organizational policies and regulations.

**Examples Scenario:** If there's a need to remove certain access rights deemed excessive or no longer necessary from a group of roles, configuring this parameter with the ID of a workflow designed for this purpose will automate the execution, effectively updating the roles without manual intervention.

**Related Settings:** 

- `DefaultDomainForMixedLogin`
- `RemoveRolesWorkflowTypeId`

**Best Practices:** configure when
- You have established a workflow specifically designed for managing role modifications, including the removal of activities.
- There's a clear understanding of the roles and activities being targeted for removal to ensure that essential access rights are not inadvertently revoked.

avoid when
- There's no dedicated workflow for role modification in place. Blindly setting this parameter without the proper infrastructure can lead to unintended consequences.
- The impact of removing specific activities from roles has not been fully assessed.