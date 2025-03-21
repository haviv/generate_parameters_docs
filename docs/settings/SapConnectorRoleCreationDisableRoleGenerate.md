**Sap Connector Role Creation Disable Role Generate**

**Technical Name:** SapConnectorRoleCreationDisableRoleGenerate

**Category:** Configuration

**Default Value:** 0

**Impact Level:** Medium

**Description:**
This parameter controls the behavior of role creation within the SAP connector. When enabled, the system will not generate new SAP roles if the specified roles do not exist within the SAP environment. This parameter ensures that role creation adheres to specific compliance and governance models by preventing unauthorized or accidental role generation.

**Business Impact:**
Enabling this setting can significantly affect how security, risk, and compliance postures are managed within an organization's SAP landscape. It ensures that only pre-approved roles are used, thereby reducing the risk of unauthorized access or unintended privilege escalation. It aligns with best practices in controlling role creation, ensuring that all changes are subject to proper governance processes.

**Technical Impact when configured:**
When configured, SAP connectors will default to not creating new roles if they are not found. This affects how updates and changes are propagated in the SAP environment, particularly when roles assumed to exist are missing. It necessitates a more rigorous role management process, ensuring all roles are predefined and created through controlled processes.

**Examples Scenario:**
Consider an organization that must comply with strict audit requirements regarding role management and provisioning within its SAP systems. By setting `SapConnectorRoleCreationDisableRoleGenerate` to a non-zero value, this organization can ensure that no new roles are created without going through a formal review and creation process. This helps to enforce strict governance and compliance with internal and external audit requirements.

**Related Settings:** AutomaticWorkflowSoDMitigatedFixedDayInMonth

**Best Practices:** 
- Configure when: Organizations require strict control over role creation within their SAP systems to comply with internal governance and external compliance requirements.
- Avoid when: Role creation needs to be dynamic and automated based on real-time needs without manual intervention.