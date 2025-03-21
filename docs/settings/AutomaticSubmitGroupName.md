# Automatic Submit Group Name

**Technical Name:** AutomaticSubmitGroupName

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Automatic Submit Group Name parameter is designed for usage within the Pathlock GRC platform's workflow automation features. It facilitates the automatic forwarding and processing of workflow items that have not been handled during specified intervals, ensuring a seamless and efficient certification process. 

**Business Impact:**

By utilizing the Automatic Submit Group Name, organizations can minimize delays in their workflow processes, especially in certification or approval tasks. This ensures that critical security, compliance, and risk management activities are not hindered by manual process bottlenecks, contributing to the overall governance and compliance posture of the organization.

**Technical Impact when configured:**

When configured, this parameter automatically forwards workflow items at intervals, based on preset criteria such as approval status and comments from previous steps. This promotes continuity in workflow processes, reduces the need for manual intervention, and ensures timely completion of workflow tasks.

**Example Scenario:**

A company has a certification process for user access reviews that needs to be completed within a certain timeline. Setting up the Automatic Submit Group Name would allow items that have not been addressed by the end of a review step to be automatically forwarded to the next step or designated group, ensuring that the process continues to move forward without unnecessary delay.

**Related Settings:** 

- `MaximumWorkflowUploadFileSize`: This setting could be related in scenarios where large files are part of the workflow items being automatically submitted.

**Best Practices:** 

- **configure when:** Environments with high volumes of workflows that require consistent movement and processing of tasks, to ensure no item is stalled due to oversight.
  
- **avoid when:** Workflows that require detailed manual review and intervention at every step, where automatic forwarding could bypass necessary checks.