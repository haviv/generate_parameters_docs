# Power Shell Exe Path

**Technical Name:** PowerShelllExePath

**Category:** Configuration

**Default Value:** (No default value specified in provided references)

**Impact Level:** High

**Description:** The `PowerShelllExePath` parameter specifies the filesystem path to the PowerShell executable. This setting is essential for executing PowerShell scripts or commands from within the Pathlock GRC platform, particularly in workflows that include custom methods or actions.

**Business Impact:** Correct configuration of the PowerShell Executable Path is vital for ensuring that automated tasks and scripts run smoothly and securely within the Pathlock GRC environment. Failure to correctly configure this path can lead to the inability to perform crucial automated security, compliance, and administration tasks, potentially putting the organization's data at risk.

**Technical Impact when configured:** Properly configuring the `PowerShelllExePath` enables the Pathlock GRC platform to:
- Execute PowerShell scripts efficiently and securely.
- Leverage customized automation within compliance and security workflows.
- Ensure that administrative tasks are performed with the correct permissions and settings.

**Examples Scenario:** Automating the generation of compliance reports using PowerShell scripts. With the `PowerShelllExePath` correctly configured, Pathlock GRC can execute a custom PowerShell script to gather required data, generate the report, and distribute it to the relevant stakeholders, all as part of an automated workflow.

**Related Settings:** N/A

**Best Practices:** 
- **Configure when:** Custom workflows or methods that require PowerShell scripting are in use.
- **Avoid when:** If PowerShell is not utilized within the platform’s workflows or if there are security concerns regarding the execution of scripts from third-party sources.