# ReleaseTransport

**Category:** Workflow

**Description:** The `ReleaseTransport` action is designed to automate the process of releasing transports within an SAP environment, directly integrating with SAP systems through the BaseSapWASConnector. When executed, this action retrieves the specified transport number from the input parameters and uses the SAP connector to release the transport. This automation facilitates seamless updates and deployments, minimizing manual efforts and enhancing system governance.

**Parameters:**

- Basic:
    - Name: TransportNo
    - Description: The unique identifier of the SAP transport request to be released. This parameter is vital for identifying which transport should be processed by the SAP connector.
    - Default value: None
    - Mandatory: Yes
    
    - Name: SystemId
    - Description: Identifies the targeted SAP system by its unique ID, establishing the context in which the transport release operation should be performed.
    - Default value: None
    - Mandatory: Yes

- Advanced:
    - Name: NewRoleName
    - Description: Specifies a new role name to be associated with the release action. This parameter is optional and might be used for advanced configuration or logging purposes.
    - Default value: None
    - Mandatory: No

**Business impact:** The `ReleaseTransport` action streamlines the deployment process of SAP transports, significantly reducing the manual workload and the potential for human error. By automating transport releases, organizations can ensure that their SAP environments are updated promptly and accurately, thereby maintaining system integrity and supporting compliance needs. This action plays a critical role in change management workflows, making it easier for administrators and developers to manage system updates.

**Example of usage:** To release a transport with the number "TR12345" in the SAP system identified by the system ID "10," the action can be called with the following parameters:

- TransportNo: TR12345
- SystemId: 10

This would initiate the process of releasing the specified transport in the targeted SAP system, leveraging the system's configured SAP connector for execution.

**Prerequisites:** Users must have appropriate permissions within the SAP environment to release transports. Additionally, the SAP system must be configured correctly within the Pathlock Cloud platform, including the setup of the BaseSapWASConnector for the specified system ID.

**Error Handling and Troubleshooting:**

- Common Error: "Transport number not found"
    - Cause: The specified transport number does not exist within the SAP system.
    - Solution: Verify that the transport number is correct and try again.
    
- Common Error: "System ID not configured"
    - Cause: The specified system ID does not match any configured SAP systems in the Pathlock Cloud platform.
    - Solution: Ensure that the system ID is correct and that the corresponding SAP system is correctly configured in Pathlock Cloud.

- Common Error: "Insufficient permissions"
    - Cause: The executing user lacks the necessary permissions to release transports in the SAP system.
    - Solution: Verify the user's permissions within the SAP environment and ensure they have the authority to execute transport releases.