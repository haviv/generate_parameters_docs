# Role Types To Assign By Child Roles

**Technical Name:** RoleTypesToAssignByChildRoles

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used within the initiation step of a workflow to determine the types of roles that can be assigned based on the roles already assigned to a child entity. It helps in ensuring that role assignments are carried out in compliance with established hierarchy and dependency rules.

**Business Impact:**

Proper configuration of this parameter supports compliance with internal and external policy regulations by enforcing role hierarchy within workflow processes. Misconfiguration might lead to unauthorized access or violation of segregation of duties (SOD) principles, potentially resulting in audit findings or security breaches.

**Technical Impact when configured:**

- Ensures that roles assigned during the StartStep workflow action adhere to predefined organizational role hierarchies.
- Prevents the automatic removal of critical roles such as "Domain Users" during the reassignment process, a specific customization added for Bank Yahav.
- Supports compliance efforts by enforcing role assignment policies directly within the workflow actions.

**Examples Scenario:**

When a new employee is onboarded, the `RoleTypesToAssignByChildRoles` parameter ensures that the employee is only assigned roles that are appropriate given their position and the roles of their direct reports. This avoids situations where an employee might be incorrectly granted managerial roles without the necessary preliminary roles.

**Related Settings:**

- RequestSubmittedShowFeedback

**Applicable Workflows Actions:**

This attribute is not applicable as specified by the guidelines.

**Best Practices:** 

- **Configure when:** Setting up or revising workflow steps to ensure role assignments are made according to organizational policies and hierarchies.
- **Avoid when:** The automation or workflow in question does not involve role assignment or when role assignments do not follow a hierarchical structure.