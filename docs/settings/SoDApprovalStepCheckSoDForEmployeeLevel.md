# SoD Approval Step Check SoD For Employee Level

**Technical Name:** SoDApprovalStepCheckSoDForEmployeeLevel

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the Separation of Duties (SoD) check at an employee level during the workflow step. It is designed to enhance security and compliance by preventing conflicts of interest through a more granular SoD enforcement.

**Business Impact:**

Enabling this setting ensures that roles or permissions assigned to employees are carefully vetted to prevent any potential conflicts of interests, thereby safeguarding the organization from insider threats and compliance risks.

**Technical Impact when configured:**

When configured, the system will perform additional checks for SoD at the employee level, particularly focusing on roles that are being simulated or requested for assignment. This ensures that all role assignments comply with the organization's SoD policies at a very granular level.

**Examples Scenario:**

Consider a scenario where an employee in the finance department is requesting additional access rights that would normally be restricted due to SoD rules. With this parameter enabled, during the workflow step, an additional SoD check will be performed considering the employee's existing roles and the new roles being requested. This ensures that no conflicting roles are assigned, thereby maintaining a strict adherence to SoD policies.

**Related Settings:** SoDReviewEveryMonths

**Best Practices:** configure when implementing strict SoD controls within your GRC strategy; avoid when your organization operates with a more flexible role assignment approach or when such detailed checks might hinder operational efficiency.