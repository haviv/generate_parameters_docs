# AddUserGroupRule

**Category:** User Management

**Description:** The `AddUserGroupRule` action automates the process of associating a user with a specific user group based on Active Directory (AD) username. It evaluates given parameters - the name of the user group and the AD username, constructs a query condition, and applies it to the database to update the user's group affiliations. This action ensures users are allocated to the correct groups according to their roles and access requirements.

**Parameters:**

- Basic:
    - Name: AssignUserGroup
    - Description: The name of the user group to which the user will be assigned. This parameter is used to locate the group's ID in the database and link it with the user.
    - Default value: None
    - Mandatory: Yes
  
    - Name: ADUserName
    - Description: The Active Directory username of the user. This parameter is used to build a query condition that matches the user in the system.
    - Default value: None
    - Mandatory: Yes

**Business impact:** Automating user group assignments enhances the efficiency of access management processes, reduces manual errors, and ensures compliance with organization-wide security policies. By dynamically assigning users to appropriate groups based on their roles, organizations can streamline access to resources, enforce segregation of duties (SOD), and efficiently manage risk and compliance requirements.

**Example of usage:** An administrator wants to assign a newly onboarded employee, with the AD username "john.doe", to the "FinanceTeam" user group to grant him the necessary access rights. By using the `AddUserGroupRule` action with the parameters `AssignUserGroup = "FinanceTeam"` and `ADUserName = "john.doe"`, the system will automatically update the user's group affiliations, thereby ensuring the user has the correct access permissions from day one.

**Prerequisites:** 

- The user executing this action must have adequate permissions to modify user groups and user details within the system.
- The specified user group name must exist in the system.
- The AD username provided must correspond to a valid user in the database.

**Error Handling and Troubleshooting:**

- If the user group name or AD username is not provided (null or empty), the action will not perform any operation. Ensure that all required parameters are provided.
- If the user group name does not exist in the database, the action will not perform any modifications. Verify the user group name and ensure it matches with those available in the system.
- For issues related to database connections or permissions, ensure that the executing user has the necessary database rights and that the database server is accessible.
- If modifications do not appear to be applied, check the database logs for any errors during the transaction and ensure that the system has sufficient rights to commit changes.