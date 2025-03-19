Action Name: AddRoleToTransport

**Category:** Workflow

**Description:** 

The `AddRoleToTransport` action is integral within the Pathlock Cloud's workflow engine, primarily focusing on automating the process of associating SAP roles to transport requests. It serves as a bridge between identity management tasks and system-specific operations, facilitating smoother transitions and deployments of role changes across environments. The action extracts requisite parameters, such as system identifiers and role names, to initiate a mass transport operation within an SAP system, effectively streamlining the process of role adjustments and deployments without manual intervention.

**Parameters:** 

- Basic:
    - Name: SystemId
    - Description: Identifies the specific system where the role will be added to a transport. It is utilized to initialize the context for connecting to the correct system.
    - Default value: None
    - Mandatory: Yes
    - Name: TransportNo
    - Description: The transport request number to which the new role will be added. This parameter allows the action to specifically target and update the desired transport request.
    - Default value: None
    - Mandatory: Yes
    - Name: NewRoleName
    - Description: The name of the new role to be added to the transport request. This is crucial for identifying which role is being operated upon within the workflow.
    - Default value: None
    - Mandatory: Yes

- Advanced:
    - Name: TargetSystemIdBasedOnParameters
    - Description: Optionally overrides the `SystemId` if provided. This allows dynamic targeting of systems based on workflow parameters, thereby enhancing flexibility in role deployment scenarios.
    - Default value: None
    - Mandatory: No

**Business impact:**

This action automates the addition of roles to SAP transport requests, thereby accelerating the deployment process and minimizing manual errors. It ensures that role updates are propagated efficiently across systems, maintaining system integrity and compliance with identity and access management policies. This capability is crucial for enterprises looking to streamline their SAP role management processes, ensuring agility in access governance and compliance tasks.

**Example of usage:**

In a scenario where an organization needs to quickly add a newly created role, `FinanceViewer`, to a transport request `TR12345` in their SAP system with an ID of `100`, the workflow can be configured to automate this process using the `AddRoleToTransport` action. The organization benefits from reduced manual intervention and faster deployment times, thereby enhancing the efficiency of their identity and access management practices.

**Prerequisites:**

- Appropriate permissions to execute transport operations within the target SAP system.
- Valid inputs for the `SystemId`, `TransportNo`, and `NewRoleName` parameters.
- The SAP system connector must be properly configured within the Pathlock Cloud environment.

**Error Handling and Troubleshooting:**

- If the action fails due to an invalid `SystemId`, verify that the provided ID corresponds to a correctly configured and accessible system within the Pathlock Cloud platform.
- A missing or incorrect `TransportNo` will prevent the operation from proceeding. Ensure that the transport request exists and is accessible.
- Errors related to the addition of the role to the transport may indicate permission issues or misconfigurations within the SAP system. Review system logs and validate connector configurations.
- Advanced parameter `TargetSystemIdBasedOnParameters` should be used judiciously. Incorrect system targeting can lead to unintended consequences. Always verify input values if this parameter is utilized.