### CreateRoleAction

**Category:** User Management

**Description:** The `CreateRoleAction` is designed to automate the process of creating roles within an organization's identity management system. This action, when executed, initializes the appropriate system context based on the provided system ID, and attempts to create a new role with specific characteristics (name, path, type, and description). It conditionally assigns the role to users if specified. This action interacts with the system's connector to create the group in the system and update the database accordingly. It is capable of handling roles across different systems, including conditional handling for non-SAP connectors and extending its function to systems of type "Exchange" when specific conditions are met.

**Parameters:**
- Basic:
    - Name: RoleName
      Description: The name of the role to be created. It is used as a key identifier for the role across the system.
      Default value: N/A
      Mandatory: yes
    - Name: Path
      Description: The organizational path in which the role should be created. This parameter helps in structuring roles hierarchically.
      Default value: N/A
      Mandatory: no
    - Name: Type
      Description: Defines the role type, influencing role creation logic especially regarding system-specific behaviors.
      Default value: N/A
      Mandatory: yes
    - Name: AssignToUsers
      Description: A flag determining whether the newly created role should be assigned to users. Utilized in a loop to assign the role to specified user IDs.
      Default value: false
      Mandatory: no
- Advanced:
    - Name: Description
      Description: Provides a detailed description of the role's purpose and scope within the organization, enlightening administrators about its use.
      Default value: N/A
      Mandatory: no

**Business impact:** The creation of roles through `CreateRoleAction` directly impacts an organization's ability to efficiently manage access and permissions, ensuring that users have appropriate access to system resources. Automating role creation simplifies the onboarding process, enhances security by accurately assigning permissions, and ensures compliance with internal policies or external regulations by standardizing role deployment.

**Example of usage:**
An administrator wants to create a new role “Manager” within the “Sales” department that allows access to specific resources. The role is to be assigned to certain users immediately upon creation.

```csharp
WorkflowActionPramaters parameters = new WorkflowActionPramaters {
    { "RoleName", "Manager" },
    { "Path", "/Departments/Sales" },
    { "Type", "Security" },
    { "Description", "Managers in the sales department with access to budget and forecast reports." },
    { "AssignToUsers", "true" }
};

CreateRoleAction action = new CreateRoleAction();
action.Perform(parameters);
```

**Prerequisites:** Before executing the `CreateRoleAction`, the user must have administrative permissions within the identity management system to create roles. Additionally, the system ID must be correctly specified to ensure the action is performed within the correct system context.

**Error Handling and Troubleshooting:**
- Common error scenarios include invalid parameters (e.g., missing RoleName), lack of permissions to create roles, or errors in system initialization.
- Probable causes may involve configuration issues, database connectivity problems, or system-specific constraints.
- Recommended solutions include verifying all required parameters are provided, ensuring the user has appropriate permissions, and checking system logs for initialization errors. For persistent issues, consulting system-specific documentation or support may be necessary.