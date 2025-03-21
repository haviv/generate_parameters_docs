# Run Impact Analysis On Workflow Role Owner Change

**Technical Name:** RunImpactAnalysisOnWorkflowRoleOwnerChange

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:** 

This parameter controls whether an impact analysis is run whenever there is a change in the ownership of a workflow role within the Pathlock Cloud GRC platform. When enabled, it ensures that any alterations to role ownership go through a thorough assessment to identify potential impacts on security, compliance, and risk posture.

**Business Impact:** 

Enabling this feature helps in maintaining a robust security and compliance posture by ensuring that any changes to role ownership do not inadvertently lead to violations of access control policies or segregation of duties (SoD) rules. It prevents unauthorized access and reduces the risk of fraud, thereby protecting sensitive information and maintaining regulatory compliance.

**Technical Impact when configured:** 

When this parameter is enabled, the system will automatically trigger an impact analysis process whenever a role owner is changed. This process assesses the implications of the change across the organization's GRC framework, including potential SoD conflicts, access policy violations, and compliance issues. As a result, administrators can make informed decisions and take necessary actions to mitigate any identified risks.

**Examples Scenario:**

- **Before Promoting an Employee:** Before promoting an employee to a new position that involves ownership of critical workflow roles, enabling this parameter allows for an assessment of how this change affects access controls and compliance requirements, ensuring that the promotion does not introduce any security or compliance risks.

- **Reorganizing Departments:** In the event of a departmental reorganization that requires transferring role ownership between managers, this feature will evaluate the impact of these changes on the security and compliance posture, helping to maintain integrity and compliance throughout the reorganization process.

**Related Settings:** 

- EnableActiveDirectoryLastLogonDates (While not directly related, understanding when users last logged on can be important for overall security and compliance posture in context with role ownership changes).

**Best Practices:** 

- **Configure when:** Major reorganizations or role changes are planned, or when the organization operates in a highly regulated industry where compliance and security are paramount. 

- **Avoid when:** If the organization has a very stable role structure with infrequent changes, or if the performance impact of running additional analyses outweighs the security benefits in a specific environment.