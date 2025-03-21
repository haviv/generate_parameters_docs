# Sample Low Case Roles

**Technical Name:** SampleLowCaseRoles

**Category:** User Management

**Default Value:** NA

**Impact Level:** Medium

**Description:**

The `SampleLowCaseRoles` parameter influences the handling and representation of user roles within the Pathlock Cloud GRC platform, with a particular focus on their case sensitivity and hierarchical structure. It ensures consistent role definitions across various SAP components connected within the system.

**Business Impact:**

Proper configuration of this parameter supports the integrity of role-based access control (RBAC) policies, mitigates the risk of unauthorized access, and enhances compliance with internal and external audit requirements by maintaining uniform role definitions.

**Technical Impact when configured:**

When properly configured, `SampleLowCaseRoles` facilitates accurate role synchronization, ensuring that role changes (including creation and modification dates) are correctly captured and parent-child role relationships are consistently maintained. This accuracy is crucial for reliable access rights management and reporting.

**Examples Scenario:**

- An organization implements the `SampleLowCaseRoles` parameter to standardize role names in lower case for all SAP connectors, thereby ensuring that role-based access controls are applied uniformly, regardless of case sensitivity issues that may arise during role synchronization or reporting processes.

**Related Settings:**

- RunProccessOutProccess
- RunSoDCheck
- RequestDeniedTemplateId
- RequestRecievedTemplateId

**Best Practices:** configure when standardization and uniformity of role names across different systems and platforms within the organization are needed; avoid when case sensitivity is required for role definitions or there are system constraints that necessitate maintaining roles in their original case.