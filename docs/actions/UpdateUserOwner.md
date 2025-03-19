# UpdateUserOwner

**Category:** User Management

**Description:** The `UpdateUserOwner` action is designed to update the employee number of a user within Pathlock Cloud's database, based on the `UserOwner` parameter provided. The action searches for the user by their `UserId`, associated with the `WorkflowInstance`, and then extracts and updates the employee number from the `UserOwner` parameter. This operation primarily involves the manipulation of user data to reflect changes in user ownership or employee details correctly in the system.

**Parameters:**

_Basic:_

- Name: UserOwner
- Description: A string parameter that specifies the new user owner's employee number and additional identifiers, separated by a dash ("-"). The employee number is extracted as the first part before the dash and used to update the user’s record.
- Default value: N/A
- Mandatory: Yes

**Business impact:** Updating the user owner or employee number in the system is critical for maintaining accurate user management and access control records. This action impacts how user data is correlated with their permissions and roles within the Pathlock Cloud platform. By ensuring that user records are up-to-date, organizations can prevent unauthorized access and minimize security risks, while maintaining compliance with internal policies and external regulations.

**Example of usage:** Suppose an employee changes their department or their role within the organization is redefined. The `UpdateUserOwner` action can be triggered by a workflow to update the employee's number in the system, ensuring that the user’s access rights and permissions are correctly aligned with their new role or department.

**Prerequisites:** The user must exist in the system, and the `WorkflowInstance.UserId` must correctly reference this user. The caller must have permissions to execute user update operations within the Pathlock Cloud platform.

**Error Handling and Troubleshooting:**

- **Error: User not found** – This error indicates that there is no user matching the `UserId` provided in the `WorkflowInstance`. Check that the `UserId` is correct and corresponds to an existing user in the system.
- **Error: Invalid UserOwner format** – If the `UserOwner` parameter does not contain the expected format or is missing the dash ("-"), ensure the input follows the correct format ("[EmployeeNumber]-[AdditionalInfo]").
- **Error: Database submission failed** – This can occur due to database constraints or connectivity issues. Verify that the database is accessible and that the user record does not violate any database constraints (e.g., unique constraints on the employee number).