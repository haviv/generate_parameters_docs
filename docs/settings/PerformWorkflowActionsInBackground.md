# Perform Workflow Actions In Background

**Technical Name:** PerformWorkflowActionsInBackground

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** This setting allows the system to perform workflow actions in the background, without needing to wait for user interaction or the completion of other tasks. It helps in streamlining processes and improves efficiency in handling workflows.

**Business Impact:** Enabling this feature can significantly impact how quickly and efficiently workflow tasks are completed within the organization. It enables faster processing of workflows, such as approvals or updates, leading to quicker decision-making and improved overall productivity.

**Technical Impact when configured:** When this parameter is configured to perform workflow actions in the background, the system automatically progresses through workflow steps without manual intervention. This could include attaching files to workflow instances or processing background checks and validations as part of the workflow.

**Examples Scenario:** If a user initiates a request that requires multiple approvals from different departments, configuring this parameter to enable background processing means that as soon as one department approves the request, it automatically moves to the next department without any delay, speeding up the entire approval process.

**Related Settings:** 

**Best Practices:** configure when large volumes of workflow actions are common, and immediate processing is beneficial. Avoid when workflows require sequential user inputs and validations that need to be manually verified before proceeding.