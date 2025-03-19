# Delete User Profile Folder

**Category:** User Management

**Description:** The Delete User Profile Folder action is designed to programmatically delete a user's profile folder based on their home directory attribute. This action is triggered within a workflow to manage user access and clean up user data upon deprovisioning. It operates by first validating the existence of the home directory attribute in the user's profile, then checking if the specified folder exists, and if so, removing it along with all of its contents.

**Parameters:**  
- Basic:
    - **Name:** homeDirectoryAttribute
    - **Description:** The attribute name in the user profile that stores the path of the user's home directory. It’s used to locate the profile folder that needs to be deleted.
    - **Default value:** User-homedirectory
    - **Mandatory:** Yes

**Business impact:** Deleting a user's profile folder is a critical step in the user deprovisioning process, ensuring that sensitive information and personal data are not left accessible after the user's departure. This action aids in maintaining data privacy standards and helps in efficient user management. It directly supports compliance with internal data handling policies and potentially with external regulations regarding data privacy and protection.

**Example of usage:** An example of using the Delete User Profile Folder action would be during the offboarding process of an employee. When the HR system triggers the workflow for employee offboarding, this action could be invoked to securely and efficiently remove the employee's profile folder, ensuring that no sensitive data is left behind.

**Prerequisites:** Users must have administrative permissions on the file system to delete directories. Additionally, the workflow instance must have access to the user's profile attributes, specifically the user's home directory path.

**Error Handling and Troubleshooting:**  
- **Error:** "Attribute not found: User-homedirectory"
    - **Cause:** The user's profile does not contain the homeDirectory attribute.
    - **Solution:** Ensure the user's profile is correctly set up with a home directory attribute.
- **Error:** "Folder not defined for user"
    - **Cause:** The home directory path is missing or empty in the user's profile.
    - **Solution:** Confirm the user's home directory path is present and correct.
- **Error:** "Could not delete folder: [Error Message]"
    - **Cause:** Various, including insufficient permissions, folder in use, or system error.
    - **Solution:** Verify the application has the necessary permissions, ensure the folder or its contents are not in use, and check for system issues that might prevent deletion.