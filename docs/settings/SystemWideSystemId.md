# HR source system

**Technical Name:** SystemWideSystemId

**Category:** Configuration

**Default Value:** (not specified)

**Impact Level:** High

**Description:**

The `SystemWideSystemId` parameter is utilized across the Pathlock Cloud GRC platform to identify and manage system-wide settings, particularly in relation to user management and workflow processes. This parameter ensures that configurations or actions can be applied universally across all systems integrated into the Pathlock platform, enhancing both security and compliance measures by maintaining a consistent policy application.

**Business Impact:**

Implementing the `SystemWideSystemId` effectively allows organizations to streamline their GRC processes, ensuring uniformity in compliance and security policies. This is crucial for organizations with complex IT environments, as it simplifies management tasks and reduces the risk of oversight or non-compliance due to disparate system configurations.

**Technical Impact when configured:**

Once configured, `SystemWideSystemId` influences various functionalities within the Pathlock platform, including user addition to approval groups, employee position management, and the initiation of workflows. It enables these actions to adhere to system-wide settings, thus acting as a centralized point of control for system-wide GRC management.

**Examples Scenario:**

A scenario where `SystemWideSystemId` is pivotal includes the automation of user role assignments in compliance with SOD (Segregation of Duties) policies. By configuring this parameter, an organization can ensure that when a user is added to an approval group or when there's a query for the last employee in a position as part of a workflow action, these operations respect the organization-wide settings for SOD, thereby mitigating risk.

**Related Settings:** 

- `CommonSettings.Default.IsCloud`
- `CommonSettings.Default.SystemWideSystemId`

**Applicable Workflows Actions:** 

- AddUserToApprovalGroup
- FindLastEmployeeInPosition
- StartWorkflows

**Best Practices:** configure when initiating system-wide changes that must be reflected across all integrated systems, avoid when changes are meant for a specific system context only.