# Hide System Field In Workflow Requests

**Technical Name:** HideSystemFieldInWorkflowRequests

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:** Determines whether system fields should be hidden in workflow requests, enhancing the user interface by decluttering unnecessary information for end users.

**Business Impact:** Reducing the visibility of system fields in workflow requests streamlines the approval process by focusing on essential fields, thus potentially reducing the time for decision-making in workflow-related tasks and approvals.

**Technical Impact when configured:** When enabled, this setting omits system fields from being displayed in the workflow request forms. This action can lead to a cleaner interface, enabling users to concentrate on pertinent data, thereby improving user experience and efficiency in processing requests.

**Examples Scenario:** In a scenario where an organization wants to streamline the process of help desk ticket approvals, enabling this parameter would hide redundant system fields from the request form, allowing the approver to quickly identify and process relevant information.

**Related Settings:** 

- `ShowDefaultRolesForExternalUsers`
- `ExternalUserEnableComments`

**Best Practices:** 

- **Configure when:** a simplified user interface is necessary for specific workflows to enhance decision-making efficiency without the distraction of system-generated fields.
  
- **Avoid when:** comprehensive detail, including system fields, is required for making informed decisions on workflow requests.