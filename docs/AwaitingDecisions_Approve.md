**Awaiting Decisions Approve**

**Technical Name:** AwaitingDecisions_Approve 

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AwaitingDecisions_Approve` parameter is used to control the behavior of automated approval processes within the Pathlock Cloud GRC platform, specifically in the context of user data owner approvals for access violations. When enabled, this setting facilitates the automatic notification to data owners when access violations occur, requiring their decision to approve or reject the access based on compliance rules.

**Business Impact:**

Enabling this parameter enhances the security and compliance posture of the organization by ensuring that any access violation or suspicious activity is promptly reviewed and approved by the designated data owner. This reduces the risk of unauthorized access and helps maintain strict adherence to internal and external compliance standards.

**Technical Impact when configured:**

When configured, the system will automatically send an email notification to the user data owner's email address whenever an access violation that requires their decision is detected. This ensures that data owners are immediately informed of potential security or compliance issues concerning their data, allowing for quicker resolution.

**Example Scenario:**

A user attempts to access a sensitive application area for which they do not have the required permissions. The Pathlock Cloud GRC platform detects this access attempt as a violation. With `AwaitingDecisions_Approve` enabled, the system automatically identifies the data owner for the violated application area and sends them an email notification requesting their approval or rejection of the attempted access.

**Related Settings:**

- CommonSettings.Default.IsValidateInstallation
- CommonSettings.Default.ShowCSG
- CommonSettings.Default.SettingsKey
- Actions_Address

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** It's crucial to have a tight grip on security and compliance, especially in sensitive data areas where access needs to be strictly controlled and monitored.
  
- **Avoid when:** If the organization does not have the bandwidth to manage the approval requests in a timely manner, or if automated decision-making is not reliable due to the complexity of access rules and exceptions.