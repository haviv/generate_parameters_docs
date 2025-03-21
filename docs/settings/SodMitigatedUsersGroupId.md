# SoD Mitigated Users Group

**Technical Name:** SodMitigatedUsersGroupId

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter identifies the group of users who have mitigations applied against identified Segregation of Duties (SoD) conflicts within the Pathlock Cloud GRC platform. Managing SoD conflicts effectively reduces the risk of fraudulent activities by ensuring that no single individual has control over all aspects of a financial transaction or process.

**Business Impact:**

Proper configuration of the SoD Mitigated Users Group is crucial for organizations to maintain compliance with regulatory requirements and to protect against the risks associated with insufficient internal controls. It facilitates targeted mitigation strategies, helping organizations to manage and reduce risk exposure from potential conflicts of interest within their user base.

**Technical Impact when configured:**

When configured, the SodMitigatedUsersGroupId parameter enables the system to recognize and categorize users who have undergone conflict mitigation. This categorization supports streamlined reporting, audit processes, and the enforcement of access controls based on mitigation status, enhancing the overall security posture and compliance stance of the organization.

**Example Scenario:**

Consider an organization with a user who requires access to both creating purchase orders and approving payments – a typical SoD conflict. By including this user in the SoD Mitigated Users Group, the organization can apply specific controls (e.g., enhanced monitoring or dual control principles) to manage and mitigate this risk. 

**Related Settings:**

- SoDApprovalStepActionId
- SoDCheckEmployeeSoDForMultiSystemOnly

**Best Practices:** 

- **Configure when:** implementing or reviewing access control policies to ensure that users with mitigated SoD conflicts are appropriately monitored and managed.
- **Avoid when:** all users are subject to the same level of scrutiny without consideration for individual risks or mitigations applied. This can lead to unnecessary administrative burden and might overlook specific risk scenarios.