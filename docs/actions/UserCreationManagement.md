Action Name: UserCreationManagement

**Category:** User Management

**Description:** The UserCreationManagement action automates the process of managing user identities across various systems, including their creation, activation, and termination. It begins by collecting details about users to be managed, segregating them into lists for creation, activation, and termination based on the input parameters and system configurations. For users to be created or activated, it generates or identifies appropriate usernames following a specified pattern set, and in cases where it's applicable, it sets or generates passwords. For termination, it identifies users in non-requested systems and performs deactivation. It handles user provisioning across different system types, including AD and Exchange, with custom logic for username generation, password setting, and system-specific actions like role assignment and user activation or deactivation.

**Parameters:**
- Basic:
    - Name: SendNotificationPerSystemForUserCreation
    - Description: Determines whether a notification is sent for each system where a user is created.
    - Default value: False
    - Mandatory: No
- Advanced:
    - Name: TerminateNonRequestedSystems
    - Description: Indicates whether users in systems not requested through the current action should be terminated.
    - Default value: False
    - Mandatory: No
    - Context: Used when it's necessary to clean up user access in systems not part of the current provisioning request.
    - Name: ChangeInstanceUserOnActivate
    - Description: Specifies if the user instance should be changed upon activating a user.
    - Default value: False
    - Mandatory: No

**Business impact:** Streamlining user identity and access management processes across multiple systems significantly reduces administrative overhead, ensures timely access for new users, and improves security by deactivating access when no longer needed. Automating these processes reduces the potential for human error, enhances compliance with internal and external audit requirements, and improves overall IT service delivery.

**Example of usage:** A new employee needs to be onboarded with access to several systems. The UserCreationManagement action is configured with parameters detailing which systems the user needs access to, any specific roles or permissions, and the employee's details. The action handles all aspects of creating and activating the user accounts, assigning necessary roles, sending out notifications per system, and ensuring that any systems not required are not provisioned for access.

**Prerequisites:** Administrative privileges on the Pathlock platform are required to configure and execute this action. Appropriate permissions in targeted systems (e.g., AD, Exchange) are necessary for user creation and management. A predefined username pattern set should be configured to facilitate automatic username generation.

**Error Handling and Troubleshooting:**
- Common Error: Failure in user creation due to an existing username.
- Probable Cause: Username collision in one or more target systems.
- Solution: Ensure that the username generation pattern is correctly configured to produce unique usernames. Alternatively, manually specify a unique username using the "OverrideCalculatedUsername" parameter.

- Common Error: User not terminated in non-requested systems.
- Probable Cause: Misconfiguration of the "TerminateNonRequestedSystems" parameter.
- Solution: Verify that the parameter is set to true if terminating access in non-requested systems is desired. Review logs for any specific error messages related to system communication failures.