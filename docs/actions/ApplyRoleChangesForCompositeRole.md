# ApplyRoleChangesForCompositeRole

**Category:** User Management

**Description:** 

The `ApplyRoleChangesForCompositeRole` action is designed to dynamically manage the composition of roles within the Pathlock cloud platform, particularly focusing on SAP roles in an Identity and Access Management (IAM) context. It extends the `ApplyRoleChanges` action and customizes the filling of request details to reflect changes in child roles based on user actions in workflow instances. This action automatically processes requests to add or remove child roles associated with a composite role, ensuring that the role composition reflects current access policies and user requests. It does so by analyzing the workflow instance for affected roles, adjusting the list of child roles based on those that need to be added or removed, and then applying these changes to the composite role in question. 

**Parameters:** 

- **Basic Parameters:**
    - **Name:** RoleName
    - **Description:** The name of the composite role for which child roles are being adjusted. It is used to identify the composite role in the SAP system and retrieve its associated child roles.
    - **Default value:** None
    - **Mandatory:** Yes
    
    - **Name:** TargetSystemId
    - **Description:** The unique identifier of the target system (e.g., SAP system) where the role changes need to be applied. It ensures that the action is executed in the context of the correct system environment.
    - **Default value:** None
    - **Mandatory:** Yes

- **Advanced Parameters:**
    - **Name:** WorkflowInstance
    - **Description:** The instance of the workflow that triggered this action. It contains all the necessary context, including affected roles and additional values that might impact the execution logic.
    - **Default value:** Current workflow instance
    - **Mandatory:** Yes
    

**Business impact:** 

Implementing automated role changes through this action significantly enhances an organization's ability to maintain proper access control and compliance with identity governance policies. By efficiently managing composite roles within systems like SAP, companies can ensure that employees have access to the necessary tools and information required to perform their jobs, while also minimizing the risk associated with improper access. This automation also reduces the workload on IT and security teams by streamlining the process of role adjustments based on predefined workflow instances.

**Example of usage:** 

An organization needs to update a composite role `ManagerRole` in their SAP system to include a new child role `ProjectManager` and remove the existing `AssistantManager` role, following a change in access policy. The workflow instance captures these requests, and the `ApplyRoleChangesForCompositeRole` action is triggered to reflect these changes accurately in the SAP system.

**Prerequisites:** 

The user executing this action must have appropriate permissions within the Pathlock platform to modify roles and workflows. Additionally, the system identifiers and role names must be valid and exist within the connected SAP system(s).

**Error Handling and Troubleshooting:** 

- **Error:** "RoleName not found"
    - **Cause:** The specified composite role name does not exist in the target system.
    - **Solution:** Verify the role name and system identifier are correct and correspond to an existing composite role.
    
- **Error:** "WorkflowInstance context missing"
    - **Cause:** The action was triggered without a proper workflow instance, or necessary details are missing from the instance.
    - **Solution:** Ensure the workflow is correctly instantiated and that all required context and parameters are provided.

- **Error:** "SystemId invalid or missing"
    - **Cause:** The target system identifier is either not provided or does not correspond to a valid system.
    - **Solution:** Check the system ID for accuracy and ensure it matches the intended target system where changes are to be applied.