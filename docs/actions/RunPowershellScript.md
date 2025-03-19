# RunPowershellScript

**Category:** Workflow

**Description:**

The RunPowershellScript action automates the execution of PowerShell scripts within the Pathlock cloud environment as part of its workflow engine, facilitating a variety of tasks such as enabling mailboxes, user management, or any PowerShell-based administrative task. This action dynamically fills in script parameters with user details from the workflow instance, executes the script with specified add-ins, and handles output or errors, improving automation and self-service capabilities for system administrators and end-users.

**Parameters:**

_Basic Parameters_

- **Name:** RunPowershell_Script
  - **Description:** The PowerShell script to be executed. Scripts can perform operations like enabling a mailbox or configuring services.
  - **Default value:** None
  - **Mandatory:** Yes
- **Name:** Addins
  - **Description:** Specifies the namespaces for PowerShell add-ins required by the script, separated by commas or new lines. This allows for extending the capabilities of the PowerShell environment tailored for specific tasks.
  - **Default value:** None
  - **Mandatory:** No

_Advanced Parameters_

- **Name:** Parameter_Identity
  - **Description:** An example of a script-specific parameter that could be dynamically filled with the user's identity. This showcases how specific action parameters can be set for the PowerShell script.
  - **Default value:** $$username$$
  - **Mandatory:** No
- **Name:** Parameter_Alias
  - **Description:** Another example of a script-specific parameter filled dynamically, potentially for a user's full name or another identifier.
  - **Default value:** $$FullName$$
  - **Mandatory:** No

**Business impact:**

This action significantly enhances operational efficiency and automation capabilities within the Pathlock cloud platform. By automating the execution of PowerShell scripts, it reduces manual tasks for system administrators, streamlines user and access management processes, improves security posture through automated configurations, and enforces compliance policies effectively. It leverages the powerful scripting capabilities of PowerShell directly within Pathlock's workflows, offering flexible and powerful solutions to complex administrative tasks.

**Example of usage:**

An administrator wants to automate the process of enabling exchange mailboxes for new users as they are onboarded within the Pathlock platform. By using the RunPowershellScript action, the administrator can specify a script like `Enable-Mailbox`, along with necessary parameters such as `Parameter_Identity` set to the new user's username. This action can be integrated into an onboarding workflow, automating the mailbox creation without manual intervention.

**Prerequisites:**

- Proper permissions to execute PowerShell scripts on the target system(s).
- The necessary PowerShell add-ins installed and accessible by the Pathlock cloud platform.
- Knowledge of the PowerShell scripting language and the parameters your scripts require.

**Error Handling and Troubleshooting:**

- **Common Error Scenario:** Failure to execute the PowerShell script due to missing add-ins.
  - **Probable Cause:** The specified add-ins are not installed or incorrectly specified.
  - **Solution:** Verify that all required PowerShell add-ins are installed and correctly listed in the action parameters.

- **Common Error Scenario:** Script execution errors.
  - **Probable Cause:** Syntax errors in the PowerShell script or incorrect script parameters.
  - **Solution:** Review the PowerShell script for errors and ensure that all parameters passed to the script are correct and in the expected format. Utilize PowerShell's debugging tools to troubleshoot the script independently if necessary.