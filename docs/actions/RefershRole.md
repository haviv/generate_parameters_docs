Action Name: RefreshRole

**Category:** User Management

**Description:** The RefreshRole action is designed to update the authorization objects for a specified role or roles within the Pathlock Cloud system, particularly for environments connected to SAP systems. When executed, this action retrieves the most current set of authorization objects for each role directly from the connected system, updates the roles' authorization details in the Pathlock Cloud database, and performs a risk simulation to identify any segregation of duties (SoD) violations that the new authorizations may cause. This process helps in keeping role definitions up-to-date and in compliance with organizational SoD policies by preemptively identifying potential risks.

**Parameters:**

*Basic:*

- Name: NewRoleName
- Description: A comma-separated list of role names that the action will refresh. The action splits this input string, trims whitespace, converts each role name to uppercase, and processes each role to refresh its authorizations and evaluate for risks.
- Default value: Not applicable
- Mandatory: Yes

*Advanced:*

(none specified)

**Business impact:** Refreshing roles and evaluating them for risk in real time aids in maintaining a secure and compliant IT environment. By automating the update and risk analysis of role authorizations, companies can ensure that their access controls remain in alignment with internal security policies and external regulations. This proactive approach to role management minimizes the potential for access-related violations and the business disruptions they can cause.

**Example of usage:** In a scenario where a company has recently updated access controls within their SAP system for a role named 'FIN_MANAGER', an administrator could use the RefreshRole action with the 'NewRoleName' parameter set to 'FIN_MANAGER' to update the role's definitions in the Pathlock Cloud system. This ensures that any changes are reflected in the company's identity and access management platform, and that the role's new authorizations do not introduce any SoD risks.

**Prerequisites:** The user must have administrative privileges within the Pathlock Cloud platform to execute this action. Additionally, the system ID provided must correspond to a properly configured SAP system connection that the Pathlock Cloud platform can access. Profiles and roles to be refreshed should already exist in both the SAP system and the Pathlock Cloud database.

**Error Handling and Troubleshooting:**

- *Error: "Role not found"*
    - Cause: The role name provided does not exist in the Pathlock Cloud database.
    - Solution: Verify that the role names are correctly spelled and correspond to existing roles in both Pathlock Cloud and the connected SAP system.

- *Error: "Connection failure"*
    - Cause: The Pathlock Cloud system is unable to connect to the specified SAP system.
    - Solution: Check the system ID for accuracy and ensure that the SAP system is accessible from the Pathlock Cloud platform. Verify network connectivity and authentication details.

- *Error: "Risk analysis failed"*
    - Cause: The risk simulation for the updated role cannot be completed, possibly due to an incomplete risk configuration or database error.
    - Solution: Confirm that all necessary risk configurations and SoD rules are correctly set up in Pathlock Cloud. Check the database for integrity and accessibility issues.

For further troubleshooting, review the Pathlock Cloud system logs, or contact Pathlock Cloud support for assistance with complex issues not resolved by initial troubleshooting steps.