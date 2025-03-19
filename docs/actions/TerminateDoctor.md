# TerminateDoctor

**Category:** User Management

**Description:** 
The `TerminateDoctor` action is designed to automate the process of terminating a doctor's access within the system. It extends the `TerminateUser` action, adding the specific capability to mark a NG06 record as deleted if required. This action is performed in a multi-step process that first checks if the NG06 deletion flag is set, and if so, proceeds to delete the NG06 record for the specified doctor. Following this, it invokes the base user termination process which includes setting the user's expiration date and removing all associated roles, ensuring a thorough cleanup of the user's access and permissions.

**Parameters:** 

*Basic Parameters:*

- **Name:** DeleteNG06
    - **Description:** Determines if the NG06 record corresponding to the doctor should be marked as deleted as part of the termination process.
    - **Default value:** `false`
    - **Mandatory:** No

*Advanced Parameters:* 

_None_

**Business impact:** 
Terminating a doctor's access when they no longer require it is crucial for maintaining system security and ensuring compliance with healthcare regulations. This action directly impacts the organization's ability to manage access rights efficiently, prevent unauthorized access, and comply with audit requirements for user access termination.

**Example of usage:** 

This action would typically be invoked as part of a workflow triggered by an HR system event, such as the resignation or retirement of a doctor. The workflow would specify the `DeleteNG06` parameter based on whether the doctor's NG06 record should also be removed.

**Prerequisites:** 

- Proper permissions to execute user termination actions.
- Access rights to manage NG06 records if `DeleteNG06` is set to true.
- The invoking user must have the necessary permissions to initiate this action within the Pathlock Cloud platform.

**Error Handling and Troubleshooting:** 

- **Error:** NG06 record cannot be found or deleted.
  - **Cause:** The doctor's SAP user name may be incorrect, or there may be an issue with the system connector.
  - **Solution:** Verify the doctor's SAP user name. Ensure the system connector is properly configured and operational.
  
- **Error:** Fails to remove doctor's roles.
  - **Cause:** Role removal may encounter issues due to dependencies or external system constraints.
  - **Solution:** Manually check the roles associated with the user and ensure they can be removed without impacting other system processes. Contact system administrator if the issue persists.

- **Error:** Workflow action fails to execute properly.
  - **Cause:** Insufficient permissions or incorrect parameter configurations.
  - **Solution:** Ensure all prerequisites are met and that the `DeleteNG06` parameter is correctly set according to the requirements. Validate the executing user has the necessary permissions.