# AssignSimulationRole

**Category:** Workflow

**Description:**

The `AssignSimulationRole` action is designed for automating the process of assigning a simulation role to a user's session within the Pathlock Cloud platform. Upon execution, this action retrieves a list of available simulation roles from a specified view in the database, selects the first role from the list, and updates the workflow instance's request data to include the chosen role name. Additionally, it updates the formatted instructions of the action instance to reflect the assigned role, ensuring that subsequent steps or users are aware of the role assignment. This facilitates dynamic simulation experiences tailored to specific roles, enhancing testing or training scenarios.

**Parameters:**

_Basic:_

- Name: `Z_SimulationRoles`
  Description: Specifies the view name from which simulation roles are retrieved.
  Default value: *Not applicable* (determined by implementation context)
  Mandatory: Yes
  
- Name: `RoleName`
  Description: Column name in `Z_SimulationRoles` view to retrieve role names.
  Default value: *Not applicable* (determined by implementation context)
  Mandatory: Yes
  
_Advanced:_

- _No advanced parameters are specified in the provided code snippet._

**Business impact:**

Implementing the `AssignSimulationRole` action within workflows significantly impacts the flexibility and efficiency of role-based access testing and training within the Pathlock Cloud platform. It automates the allocation of simulation roles, streamlining the setup process for identity and GRC management scenarios. This can lead to more accurate risk calculation and compliance reporting by enabling thorough testing under varied user roles.

**Example of usage:**

A company could use the `AssignSimulationRole` action in a workflow designed to onboard new employees into their role-specific access rights simulation. As part of the onboarding workflow, this action would automatically assign a predefined simulation role to the new employee's session based on their department or job function, facilitating a tailored training experience that closely mirrors their access rights within the production environment.

**Prerequisites:**

- Appropriate permissions to execute workflow actions within the Pathlock Cloud platform.
- A defined `Z_SimulationRoles` view in the database with at least one role available for assignment.

**Error Handling and Troubleshooting:**

- **Error:** Simulation role is not assigned.
  - **Cause:** The `Z_SimulationRoles` view might be empty or not accessible.
  - **Solution:** Verify that the `Z_SimulationRoles` view exists in the database, contains at least one role, and is accessible by the workflow engine.
  
- **Error:** Changes to the request data or formatted instructions are not saved.
  - **Cause:** Database connectivity issues or transaction failures during submission.
  - **Solution:** Check database connectivity and ensure the transaction log is not full. If the issue persists, review the workflow configuration for potential conflicts or errors in the action setup.