# AddRoleToTransport

**Category:** Workflow

**Description:** The `AddRoleToTransport` action is designed to automate the process of adding a new role to a specified transport within the SAP environment. This action retrieves the system ID and transport number from the parameters, validates if a target system ID is specified, and updates the transport with the new role name using the SAP connector. The action primarily facilitates the management of role assignments in transports, which is a common requirement in identity and access management workflows, especially in SAP systems.

**Parameters:**

_Basic Parameters:_

- Name: SystemId
  - Description: The ID of the system where the transport resides. It is used to initialize the SAP system context within the workflow.
  - Default value: None
  - Mandatory: Yes

- Name: TransportNo
  - Description: The transport number to which a new role will be added. This parameter specifies the target transport in the SAP system.
  - Default value: None
  - Mandatory: Yes

- Name: NewRoleName
  - Description: The name of the new role that needs to be added to the transport. This is the role that will be mass transported into the specified transport number.
  - Default value: None
  - Mandatory: Yes

_Advanced Parameters:_

- Name: TargetSystemIdBasedOnParameters
  - Description: Optionally specifies a different target system ID for the operation, overriding the default SystemId if provided. This allows flexibility in targeting different SAP systems within the same action execution.
  - Default value: None
  - Mandatory: No

**Business impact:** Automating the addition of roles to transports significantly enhances the efficiency and accuracy of access and role management processes within SAP environments. It reduces manual errors, saves time for administrators, and ensures consistent role assignments across transports, thereby aiding in maintaining compliance and audit requirements in the identity and access management domain.

**Example of usage:** An administrator needs to add a role named "FinancialReviewer" to a transport numbered "TR1234" in the SAP system with an ID of 1. They can execute this action with the parameters set as follows:

- SystemId: 1
- TransportNo: "TR1234"
- NewRoleName: "FinancialReviewer"
  
This operation will ensure that the "FinancialReviewer" role is correctly added to the "TR1234" transport, ready to be moved across systems as required.

**Prerequisites:** The user must have sufficient permissions to manage roles and transports within the targeted SAP system. Additionally, the specific SAP connector must be properly configured to allow for the execution of transport and role management operations.

**Error Handling and Troubleshooting:**

- **Error:** Invalid SystemId or TransportNo
  - **Cause:** The specified SystemId or TransportNo does not exist or is incorrect.
  - **Solution:** Verify that the SystemId and TransportNo are correct and refer to existing entities in the SAP system.

- **Error:** Role addition failed
  - **Cause:** The operation to add the role to the transport could not be completed. This could be due to the role name being incorrect, insufficient permissions, or issues with the SAP connector.
  - **Solution:** Check the role name for accuracy, ensure the executing user has the necessary permissions, and verify the SAP connector's configuration and status.