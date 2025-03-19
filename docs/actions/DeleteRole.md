Action Name: DeleteRole

**Category:** User Management

**Description:**  

The DeleteRole action is designed to automate the process of deactivating a role within the system, specifically for systems like SAP. When triggered, the action initializes the context for the specified system, establishes a connection using the BaseSapWASConnector, and proceeds to deactivate the specified role. This action streamlines the process for administrators to manage role lifecycle within the system, reducing manual workload and preventing unauthorized access by disabling obsolete or unauthorized roles.

**Parameters:**  

_Basic:_
- Name: SystemId  
  Description: The identifier for the system where the role will be deactivated. This parameter is used to initialize the context for the specific system in which the role exists.  
  Default value: None  
  Mandatory: yes

- Name: RoleName  
  Description: The name of the role to be deactivated. This is used by the BaseSapWASConnector to specify which role should be deactivated in the system.  
  Default value: None  
  Mandatory: yes

**Business impact:**  

Deactivating roles in a timely and efficient manner is crucial for maintaining system security and compliance. The DeleteRole action aids in preventing unauthorized access and ensuring that only valid, authorized roles are active. This is especially important in environments subject to strict access controls and regulatory compliance standards. By automating this process, Pathlock Cloud enhances operational efficiency, reduces human errors, and ensures a higher level of security and compliance.

**Example of usage:**  

In a scenario where a company needs to disable a role named "FinanceManager" from their SAP system due to restructuring, the DeleteRole action can be utilized as follows:

```
WorkflowActionParameters parameters = new WorkflowActionParameters();
parameters.SetParameter("SystemId", 100);  // Assuming '100' is the identifier for the SAP system
parameters.SetParameter("RoleName", "FinanceManager");
DeleteRole action = new DeleteRole();
action.Perform(parameters);
```

This code example demonstrates how to programmatically disable the "FinanceManager" role in a specified system.

**Prerequisites:**  

1. The executing user must have sufficient permissions to deactivate roles within the specified system.
2. The system identifier (SystemId) must correspond to a valid system setup within the Pathlock Cloud platform.
3. The role name provided must exist in the system.

**Error Handling and Troubleshooting:**  

- **Error:** Role does not exist  
  **Cause:** The RoleName parameter does not match any existing role within the specified system.  
  **Solution:** Verify the role name and ensure it is correctly spelled and exists in the target system.

- **Error:** SystemId invalid or system not found  
  **Cause:** The specified SystemId does not correspond to any system set up in the platform.  
  **Solution:** Ensure the SystemId is correct and corresponds to a system that has been configured within the Pathlock Cloud platform.

- **Error:** Insufficient permissions  
  **Cause:** The user attempting to perform the action does not have the required permissions to deactivate roles.  
  **Solution:** Ensure the executing user has been granted sufficient permissions to manage roles in the system.