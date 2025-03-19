# ChangeUserOrgUnit

**Category:** User Management

**Description:** 

This action is designed to automate the process of changing a user's organizational unit (OU) within the system. It performs two main functions: removing the user's current roles associated with their previous OU and adding new roles pertinent to the new OU they are assigned to. The action is triggered within a workflow instance, ensuring that user role changes adhere to organizational and compliance standards, thereby facilitating secure and efficient access management across different organizational units.

**Parameters:**

- Basic:
    - Name: TechnicalNameForEmployeeOrganizationUnit
    - Description: The technical name identifier for the new organizational unit to which the user will be assigned. This parameter specifies the target OU by its unique name, guiding the selection of roles to be added to the user based on the new OU structure.
    - Default value: None
    - Mandatory: Yes

**Business impact:** 

Changing a user's organizational unit and associated roles through this workflow action can significantly impact security and compliance postures. It ensures that users have access only to systems and data relevant to their new roles and responsibilities, adhering to the Principle of Least Privilege (PoLP). This automation also reduces manual errors, enhances operational efficiency, and ensures quick adaptation to organizational changes like restructurings or role pivots.

**Example of usage:** 

A company undergoing a restructuring process needs to move several users to different organizational units. This action can be used within a workflow to automate the process of revoking their access to old roles and systems and granting them new access privileges as per their new departmental responsibilities.

**Prerequisites:** 

- Proper permissions to execute role changes in the system.
- The user executing this action must have access to manage roles and organizational units within the platform.
- The new organizational unit name must exist in the system's organizational structure settings.

**Error Handling and Troubleshooting:** 

- **Error:** User roles not updating correctly.
    - **Cause:** Inadequate permissions to modify user roles.
    - **Solution:** Ensure the user executing this action has the appropriate permissions to add or remove roles.
    
- **Error:** Specified organizational unit not found.
    - **Cause:** Incorrect or outdated organizational unit name provided.
    - **Solution:** Verify the organizational unit name parameter matches an existing unit in the system. Update the workflow parameter with the correct technical name.

- **Error:** Incomplete workflow action execution.
    - **Cause:** System issues or incorrect workflow configuration.
    - **Solution:** Check the system logs and ensure that the workflow configuration is correct, including all mandatory parameters.