# ApplyUAMPolicy

**Category:** User Management

**Description:** 

The `ApplyUAMPolicy` action is designed to automate the application of user access management (UAM) policies within the Pathlock Cloud environment. When initiated, this action iterates through specified policy groups and applies corresponding UAM policies to the current workflow instance. This ensures standardized access controls are enforced automatically, promoting both security and compliance across the platform. If no specific policy groups are defined, the action applies a default set of UAM policies to the workflow instance.

**Parameters:** 

- Basic:
    - Name: PolicyGroupTechnicalName
    - Description: An array of policy group names to which the UAM policies will be applied. The action separates these names by commas and applies all matching policies found in the system to the current workflow instance.
    - Default value: *None* (an empty string leads to default policy application)
    - Mandatory: No

**Business impact:** 

Implementing the `ApplyUAMPolicy` action within workflows significantly enhances the platform's security posture by ensuring that only authorized users gain access to sensitive functions and data, thus automating compliance with regulatory standards. It streamlines the management of access controls, reducing manual effort and the potential for human error.

**Example of usage:** 

A practical use case might involve a workflow triggered by a new employee's onboarding process, where various UAM policies need to be applied based on the employee's role. By specifying the relevant policy groups in the `ApplyUAMPolicy` action, the system automatically ensures the new employee is granted the correct level of access, adhering to predefined security and compliance protocols.

**Prerequisites:** 

- Administrator privileges or equivalent access rights are required to create or modify workflow actions.
- A clear understanding of the available UAM policies and their respective groupings within the Pathlock Cloud platform.
- Existing policy groups, as referenced by the action parameters, must be predefined in the system.

**Error Handling and Troubleshooting:** 

- **Error:** "Policy group not found" 
    - **Cause:** The specified policy group name does not match any existing groups within the system.
    - **Solution:** Verify the policy group names provided as parameters against the list of policy groups configured in the Pathlock Cloud platform. 

- **Error:** "Failed to apply UAM policy"
    - **Cause:** An unexpected error occurred during the policy application process, potentially due to misconfiguration or system issues.
    - **Solution:** Check the system logs for more detailed error messages. Ensure all prerequisite conditions are met and that the policies and policy groups are correctly configured. If the issue persists, contact Pathlock support for further assistance.