# GetOrCreateVMAUser

**Category:** User Management

**Description:** The `GetOrCreateVMAUser` action is designed to either retrieve or create a new Virtual Medical Assistant (VMA) user in SAP systems. Initially, it tries to find an existing VMA for a current user based on provided parameters such as employee ID. If an existing VMA is not found, it proceeds to create a new VMA. This action integrates with SAP connectors to perform operations like reading from SAP tables and creating or updating records. It's essential in managing VMAs' lifecycle within the SAP system, facilitating tasks like assigning roles, managing access, and ensuring proper workflow in user creation or retrieval processes.

**Parameters:** 
  - Basic
    - Name: GetVMAForCurrentUser
      - Description: Determines whether the action should attempt to retrieve VMA information for the currently logged-in user.
      - Default value: false
      - Mandatory: Yes

  - Advanced
    - Name: DisableHandleSpecialCharactersForVMA
      - Description: A flag to disable special character handling when generating a new VMA username. Useful in scenarios with specific username pattern requirements that exclude special characters.
      - Default value: false
      - Mandatory: No
    - Name: UpdateVmaParametersForFoundVMA
      - Description: Indicates if the action should update parameters for an already found VMA. It's used when an existing VMA needs to be updated with new information.
      - Default value: false
      - Mandatory: No

**Business impact:** The action plays a critical role in maintaining efficient user management and access control mechanisms within the SAP environment. Automating the VMA creation and retrieval process reduces manual errors, ensures compliance with internal policies, and enhances security by ensuring that VMAs are correctly managed and assigned appropriate roles and permissions.

**Example of usage:** 
A scenario where a healthcare practitioner's assistant needs access to the SAP system for retrieving patient information. When the assistant logs in, the system, through this action, checks if the assistant already has a VMA. If not, the system will automatically create one, ensuring the assistant gets timely and secure access to necessary data without manual intervention.

**Prerequisites:** 
- SAP system connectivity and credentials.
- Proper configuration in `ProfileTailorContext` and `CommonSettings`.
- Relevant SAP connector with access to create and read VMA data.

**Error Handling and Troubleshooting:** 
- **Error:** VMA not found
  - **Cause:** The action could not find an existing VMA for the given user.
  - **Solution:** Ensure the user's identifier value is correct and matches the records in the SAP system. If the issue persists, check SAP connectivity and permissions.
  
- **Error:** Could not create new VMA
  - **Cause:** An issue occurred while creating a new VMA, possibly due to incorrect parameters or SAP system restrictions.
  - **Solution:** Verify custom parameters and ensure that the SAP connector has sufficient permissions to create new records. Review `CreateNewVMA` method implementations for potential issues.