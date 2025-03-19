# UpdateSRMOrgUnits

**Category:** User Management

**Description:** This action is designed to automate the process of updating SRM (Supplier Relationship Management) organizational units within the Pathlock cloud platform. It involves reading buyer codes from a source system, determining if updates are needed in the target system, and executing those updates through batch input processing. The action caters to scenarios where employee positions and organizational units undergo changes that need to be reflected in the SRM system to maintain accurate and up-to-date user access and roles within the organization.

**Parameters:** 

- Basic:
    - Name: UpdateSRMOrgUnits_DataReadSystemId
    - Description: The system ID from which to read data. This parameter specifies the source system ID used to retrieve the current organizational unit assignments and buyer codes.
    - Default value: None
    - Mandatory: Yes
  
    - Name: UpdateSRMOrgUnits_UpdateSystemId
    - Description: The system ID where updates will be applied. It identifies the target SRM system ID where the organizational unit updates will be made based on the retrieved buyer codes.
    - Default value: None
    - Mandatory: Yes

    - Name: UpdateSRMOrgUnits_BDCFileName
    - Description: The file name of the batch input session. Specifies the name of the file that contains batch input data for processing organizational unit updates in the target system.
    - Default value: None
    - Mandatory: Yes

**Business impact:** This action directly impacts the user management and access control system by ensuring that organizational unit updates are accurately reflected in the SRM system. It helps maintain compliance with internal policies and external regulations by ensuring that user roles and access rights are aligned with their current organizational units. Efficient and automated updating reduces manual workload, decreases the potential for errors, and helps ensure that access controls remain accurate and effective.

**Example of usage:** A company undergoes a reorganization that affects multiple employees' organizational units and associated SRM buyer codes. Rather than manually updating each user's information in the SRM system, the `UpdateSRMOrgUnits` action can be configured and executed to automatically read the new organizational data from the HR system, determine the necessary updates, and apply those updates to the SRM system by processing a batch input file containing the updated information.

**Prerequisites:** 
- The user executing this action must have appropriate permissions to access both the source (for reading data) and target (for updating data) systems.
- A predefined batch input file matching the expected format must exist and be accessible to the system performing the update.
- The SAP connectors for both reading from the source system and writing to the target system must be properly configured and operational.

**Error Handling and Troubleshooting:** 
- **Error: Batch input file not found.** This error occurs when the specified batch input file cannot be located. Ensure that the file exists and that the correct path is specified in the `UpdateSRMOrgUnits_BDCFileName` parameter.
- **Error: No relevant buyer codes were found.** This indicates that the source system did not return any buyer codes for the given employee number. Verify the employee number and the data available in the source system.
- **General Troubleshooting Tips:** 
    - Check the connectivity and configurations for both the source and target systems to ensure that there are no network or authentication issues.
    - Review the action's output and event log for any indications of specific parameters or data points that may have caused the failure.
    - Ensure that all mandatory parameters are properly set and that any default values are appropriate for the current execution context.