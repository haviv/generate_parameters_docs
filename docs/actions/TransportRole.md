# TransportRole

**Category:** User Management

**Description:** The `TransportRole` action facilitates the migration of role definitions between systems within the Pathlock platform, particularly focusing on identity and access management processes. Upon execution, this action retrieves a specified role name from the workflow parameters, identifying the role to be transported. It utilizes two system identifiers: the destination system ID (where the role will be moved to) and the source system ID (where the role currently exists). The action initializes the context for the destination system and employs the system connector to transport the specified role from the source to the destination system. This process is primarily used for synchronizing access control configurations across different environments or systems.

**Parameters:**
- Basic:
    - Name: NewRoleName
      Description: The name of the role to be transported to the destination system. This parameter is utilized to identify the specific role that needs to be migrated.
      Default value: N/A
      Mandatory: yes

    - Name: SystemId
      Description: The identifier for the destination system where the role will be transported. It defines the target environment for the operation.
      Default value: N/A
      Mandatory: yes

- Advanced:
    - Name: WorkflowInstance.RequestSystemId
      Description: The source system identifier from where the role is being transported. It is extracted from the workflow instance, indicating the original environment of the role.
      Default value: Derived from the workflow instance context.
      Mandatory: no

**Business impact:** Utilizing the `TransportRole` action streamlines the process of role management across different systems within an organization. It ensures that role definitions and corresponding access controls remain consistent and up to date across all systems, thereby reducing the risk of access-related issues and improving governance and compliance with internal and external policies.

**Example of usage:** In a scenario where a company needs to synchronize their development and production environments in terms of access control, the `TransportRole` action can be used to move a newly defined or updated role from the development system (source) to the production system (destination). For example, if a new role named "AuditManager" has been created in the development environment, the action can transport this role to the production environment, ensuring consistent access rights across both systems.

**Prerequisites:** 
- The user must have administrative permissions in both the source and destination systems.
- The source and destination systems must be correctly configured and accessible within the Pathlock platform.

**Error Handling and Troubleshooting:** 
- Error: Role name not provided.
  Cause: The `NewRoleName` parameter is missing or empty.
  Solution: Ensure that the `NewRoleName` parameter is specified with the correct role name you wish to transport.
  
- Error: Destination system not accessible.
  Cause: Incorrect `SystemId` provided or the destination system is down.
  Solution: Verify the `SystemId` for the destination system and ensure that the system is operational.

- Error: Source system not found.
  Cause: The `WorkflowInstance.RequestSystemId` does not match any known source system.
  Solution: Check that the source system is correctly configured and available in the Pathlock platform.


