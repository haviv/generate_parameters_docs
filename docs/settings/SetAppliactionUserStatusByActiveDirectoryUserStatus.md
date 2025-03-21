**Technical Name:** SetApplicationUserStatusByActiveDirectoryUserStatus

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:** 

This parameter controls the synchronization of application user statuses based on the Active Directory user statuses. When enabled, the user status within the Pathlock Cloud GRC platform will automatically update to reflect changes made in the Active Directory status of the same user. This ensures user access rights within the platform remain consistent with the organization's Active Directory policies.

**Business Impact:** 

Enabling this setting can significantly streamline user access management by reducing manual efforts to keep application access rights aligned with corporate security policies. It enhances compliance with security policies by ensuring only currently authorized users have access, mitigating the risk of unauthorized access from former employees or those whose access privileges should be revoked.

**Technical Impact when configured:** 

- Automates the process of enabling or disabling user access based on the Active Directory status, eliminating the need for manual user status updates within the platform.
- Helps maintain an accurate user status, improving security and compliance with organizational policies.
- Cuts down on administrative overhead, allowing IT and security teams to focus on more strategic tasks.

**Example Scenario:** 

A company has a policy of disabling user accounts in the Active Directory immediately upon termination of employment. By configuring `SetApplicationUserStatusByActiveDirectoryUserStatus`, the user's status in the Pathlock Cloud GRC platform is automatically updated to reflect this change, thereby revoking their access rights instantaneously without manual intervention. 

**Related Settings:** 

- ServerDiscrepancyEmailTemplate
- RequestWaitingForApprovalHideMassDecline

**Best Practices:** 

- **Configure when:** You have a dynamic workforce with frequent changes in employment status, or you require strict adherence to security policies regarding user access.
- **Avoid when:** User statuses in your Active Directory do not reflect real-time employment status accurately, or if there's a delay in updating the Active Directory status upon changes in user employment status.