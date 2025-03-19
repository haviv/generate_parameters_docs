Action Name: Compare Simulation Roles

**Category:** User Management

**Description:** 

The Compare Simulation Roles action is designed to compare the authorizations of two roles within the system: the simulation role and a new role proposed by the user. It automates the validation process to ensure that the new role's permissions align with those of the simulation role. This action fetches the roles based on their names, compares their authorizations through an external gateway, and updates the workflow instance with the comparison result. Depending on the outcome, it either advances the workflow to the next step or moves it back for reevaluation.

**Parameters:** 

Basic: 
- Name: SimulationRoleName
- Description: The name of the role used as the baseline for the comparison.
- Default value: N/A
- Mandatory: Yes

- Name: NewRoleName
- Description: The name of the newly proposed role to be compared with the simulation role.
- Default value: N/A
- Mandatory: Yes

Advanced:
- Name: SystemId
- Description: The unique identifier of the system within which the roles exist. It's used to select the correct data source for the role comparison.
- Default value: Derived from the current user's system ID.
- Mandatory: Yes

**Business impact:** 

This action directly impacts the governance, risk, and compliance (GRC) measures within the organization by ensuring that new roles do not inadvertently increase risk or violate compliance policies. Ensuring role authorizations are correctly aligned with the intended permissions helps maintain secure and efficient access management, a critical component in identity and GRC platforms like Pathlock Cloud.

**Example of usage:** 

A user creates a new role intended to mirror the permissions of an existing simulation role but tailored for a specific department. By initiating the Compare Simulation Roles action, the system will automatically verify that the new role does not exceed the permissions of the simulation role, thereby maintaining compliance with corporate security policies.

**Prerequisites:** 

- Users must have the necessary permissions to create or propose new roles within the system.
- The simulation role and the new role must already exist in the system or their names must be specified correctly in the workflow request.
- Relevant system ID must be accessible to the user executing the action.

**Error Handling and Troubleshooting:** 

- If roles cannot be found: Ensure that the role names are correctly spelled and exist within the system.
- If the system returns an error during comparison: Check system connectivity and ensure the external gateway service is up and running.
- For issues with permissions or access: Verify that the executing user has the necessary rights to perform role comparisons and make changes within the workflow.
- Logs should be reviewed for any exceptions thrown during the process for a detailed understanding of underlying issues.