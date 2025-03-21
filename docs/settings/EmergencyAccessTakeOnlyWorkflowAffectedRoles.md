**Emergency Access Take Only Workflow Affected Roles**

**Technical Name:** EmergencyAccessTakeOnlyWorkflowAffectedRoles

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**
This parameter defines specific roles that will be affected during the execution of the EmergencyAccessStep workflow action. It serves as a filter to ensure that only selected roles are considered when granting emergency access, enhancing the precision and security of the access control process.

**Business Impact:**
By accurately targeting roles, organizations can minimize the risk of unnecessary access rights being granted, ensuring that emergency access is provided strictly where needed. This tightens security controls and supports compliance with internal and external access policies.

**Technical Impact when configured:**
When configured, this parameter actively influences the subset of roles eligible for emergency access adjustments during the workflow process. It ensures that changes are applied to a controlled and predefined set of roles, reducing the scope of error and the potential for unauthorized access.

**Examples Scenario:**
In an emergency situation where a senior developer needs immediate access to specific systems for rectification of a critical issue, the EmergencyAccessTakeOnlyWorkflowAffectedRoles parameter ensures that only roles relevant to the developer's requirements are affected, speeding up the access provision process while maintaining strict access control.

**Related Settings:**

**Best Practices:** configure when precise control over affected roles during emergency access is necessary; avoid when broad access adjustments are required without role-specific restrictions.