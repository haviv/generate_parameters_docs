**Action Name: Start Workflows**

**Category:** Workflow

**Description:**
The "Start Workflows" action automates the initiation of child workflows based on certain criteria derived from the current workflow instance. This action can create multiple workflows simultaneously, catering to various scenarios such as by user roles, transactions, system affiliations, or custom input values. The decision on how workflows are split and initiated is determined by specific parameters set within this action, allowing for a high degree of customization and flexibility. The action can optionally run asynchronously to improve performance and user experience by processing complex operations in the background.

**Parameters:**

- Basic
  - Name: StartWorkflows_WorkflowTechnicalName
    Description: Specifies the technical names of the destination workflows to be initiated. Multiple workflows can be specified, separated by commas.
    Default value: N/A
    Mandatory: Yes
  - Name: StartWorkflows_StartAsnyc
    Description: Determines whether the child workflows should be started asynchronously. Asynchronous execution is recommended for operations that might take a considerable amount of time.
    Default value: false
    Mandatory: No
- Advanced
  - Name: StartWorkflows_UserGroupField
    Description: Used in scenarios where workflow creation is based on user groups. Specifies the field from which to read the user group information.
    Default value: N/A
    Mandatory: No
  - Name: StartWorkflows_commentTemplate
    Description: The template for comments to be applied to each initiated workflow. Supports placeholders for dynamic data insertion.
    Default value: N/A
    Mandatory: No
  - Name: StartWorkflows_inputField
    Description: In 'Split Mode By Input', this parameter designates the form field from which the action retrieves input values to determine how many workflows to start or the criteria for each.
    Default value: N/A
    Mandatory: No

**Business impact:**
The "Start Workflows" action streamlines the process of creating related workflows based on dynamic criteria, significantly reducing manual overhead and ensuring consistent application of business rules across different workflow instances. By automating the initiation of these workflows, organizations can ensure rapid response to compliance, risk management, or operational needs, improving overall efficiency and adherence to governance policies.

**Example of usage:**
An organization uses the "Start Workflows" action within a compliance checking workflow to automatically initiate remediation workflows for each non-compliant item identified during an audit. Parameters are set to create individual workflows for each type of compliance issue, ensuring that specific remediation actions are taken according to the nature of the issue.

**Prerequisites:**
- The user must have the appropriate permissions to create workflows.
- Applicable workflow types must be predefined in the system.
- Required fields and parameters for initiating child workflows must be accurately filled out in the parent workflow.

**Error Handling and Troubleshooting:**
- **Workflow Not Started:** Ensure the technical names specified in the `StartWorkflows_WorkflowTechnicalName` parameter exist and are correctly spelled.
- **Asynchronous Execution Issues:** For workflows failing to start asynchronously, verify server configurations and ensure background processing services are running.
- **Incorrect Parameter Values:** If workflows are not initiating as expected, review the values provided in parameters, particularly in dynamic fields like `StartWorkflows_inputField`, to ensure they contain the expected values.
- **Performance Issues:** When experiencing performance degradation, consider enabling asynchronous execution if not already done and review the system's resource utilization.