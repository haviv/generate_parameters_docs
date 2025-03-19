# CreateNewUserForEA

**Category:** User Management

**Description:**  
The `CreateNewUserForEA` action automates the process of creating a new user account within the Pathlock Cloud platform, specifically catering to emergency access scenarios. It leverages existing user information and a set of predefined workflow and system parameters to generate a new user account that adheres to the specified username patterns and access roles. This process encompasses fetching relevant parameters, validating the non-existence of a proposed username in the system, creating the user with specified roles, and updating the workflow instance with the newly created user information.

**Parameters:** 

- Basic:
  - Name: default_password
    - Description: Specifies the initial password for the newly created user. This parameter is critical for account creation and is utilized during the user creation process.
    - Default value: N/A
    - Mandatory: Yes

- Advanced:
  - No advanced parameters are specifically delineated within the provided code snippet. Parameters such as username patterns and role allocations are implicitly determined by the workflow context and system configurations rather than directly supplied by the action caller.

**Business impact:**  
Creating users efficiently and securely is critical for managing access within an organization. The `CreateNewUserForEA` action directly impacts operational efficiency by automating user creation, especially in emergency access or high-priority contexts. It ensures that new users are created following predefined patterns and roles, minimizing the risk of unauthorized access and maintaining compliance with access control policies. The automation of this process reduces manual errors, saves time, and ensures that emergency access is granted swiftly and securely.

**Example of usage:**  
In an emergency situation where a user requires immediate access to a system, an administrator initiates the `CreateNewUserForEA` action through the Pathlock Cloud workflow engine. The action gets called with all necessary parameters, including a default password and the context of the emergency access request. Upon successful execution, the action creates a new user account with specified roles, allowing the user to have immediate, temporary access to the system to perform required tasks.

**Prerequisites:**  
- Administrator privileges or equivalent permissions to initiate user creation workflows.
- A pre-configured pattern set for username generation that complies with organization standards.
- Predefined roles that should be assigned to the user being created, suitable for the emergency access context.

**Error Handling and Troubleshooting:**  

- **User already exists:** If the generated username already exists within the system, the action will fail to prevent duplicate accounts. The recommended solution is to verify the username pattern configuration and ensure sufficient variability to generate unique usernames.
- **Pattern set not configured:** Without a configured pattern set, the action cannot generate a username, hence failing the user creation process. Ensure that a valid pattern set is configured for the workflow type.
- **Failure in creating user:** General failures during the user creation process are caught as exceptions. The detailed cause might vary but reviewing server logs for the exact error message is recommended. Possible causes include issues with the connection to the user management system or data validation errors. Verify system connectivity and ensure that all custom parameters adhere to expected formats and values.