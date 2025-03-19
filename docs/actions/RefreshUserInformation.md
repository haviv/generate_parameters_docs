Action Name: RefreshUserInformation

**Category:** User Management

**Description:** The `RefreshUserInformation` action is designed to update and synchronize user information within the Pathlock Cloud's Identity and Governance, Risk, and Compliance (GRC) platform. This action targets a specific user and system, refreshing the user's data based on the provided parameters. Primarily, it handles the update by fetching the user based on the current workflow system ID or a custom system ID and username provided by the action parameters. If no custom values are provided, it defaults to the user and system ID associated with the current workflow instance. This automation ensures that user information remains current and accurate across different systems within the organization, contributing to effective identity management and compliance processes.

**Parameters:**

_Basic:_
- Name: CustomSystemIdForUserReferesh
  - Description: The ID of the system for which the user information needs to be refreshed. This parameter allows the action to target a specific system outside the default system associated with the user in the workflow context.
  - Default value: None
  - Mandatory: No

- Name: CustomUserForRefresh
  - Description: The username of the user whose information needs to be refreshed. This parameter specifies the target user when different from the user executing the action.
  - Default value: None
  - Mandatory: No

_Advanced:_
- This action does not have parameters classified under advanced based on the given code.

**Business impact:** Updating user information through the `RefreshUserInformation` action directly impacts compliance and security within the organization. By ensuring user data is consistent and accurate across systems, the action helps maintain a reliable identity and access management (IAM) environment. This reliability is key in reducing security risks associated with outdated or incorrect user data, enhancing overall system integrity, and supporting compliance with various regulatory requirements.

**Example of usage:** A common scenario for using the `RefreshUserInformation` action is within a user offboarding process. When an employee leaves the company, their user information might need to be updated across multiple systems to reflect their departure. By executing this action, the organization can automate the refresh of the user's information, ensuring a timely and consistent update process.

**Prerequisites:** Before executing the `RefreshUserInformation` action, the following conditions must be met:
- The user executing the action must have permissions to access and modify user information within the targeted system(s).
- The system ID (if using a custom system) and usernames must be valid and exist within the context of the Pathlock Cloud environment.

**Error Handling and Troubleshooting:**
- **Issue:** Action fails with a system or user not found error.
  - **Probable Cause:** The specified system ID or username does not exist.
  - **Solution:** Verify the system ID and username provided in the parameters to ensure they match the records in the Pathlock Cloud environment.
  
- **Issue:** Action completes but does not update user information.
  - **Probable Cause:** Insufficient permissions or locked user accounts.
  - **Solution:** Check the user account executing the action for adequate permissions and ensure the target user account is not locked or restricted.
  
For further issues or troubleshooting, consult the Pathlock Cloud support documentation or contact support directly.