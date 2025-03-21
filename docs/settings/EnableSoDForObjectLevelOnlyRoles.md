# Enable SoD For Object Level Only Roles

**Technical Name:** EnableSoDForObjectLevelOnlyRoles

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether Separation of Duties (SoD) controls are applied specifically to roles defined at an object level, enhancing targeted security measures within the system.

**Business Impact:**

Configuring this parameter to enforce SoD at an object level only can significantly mitigate the risk of unauthorized access or fraudulent activities by limiting user abilities based on their specific roles and the data they are allowed to access or manipulate. This focus enhances compliance with internal policies and regulatory standards.

**Technical Impact when configured:**

When enabled, the system will generate events and checks for SoD violations only for roles that are defined at the object level. This means that broad or general roles that do not specify object-level permissions will not be subject to SoD checks, potentially streamlining the process for roles with wider system access while still maintaining strict controls where they are most needed.

**Examples Scenario:**

A user assigned with two roles, where one role allows viewing financial reports (ReportViewer) at an object level, and another role grants the ability to modify financial records (FinanceEditor) also at an object level. Enabling this parameter will ensure that SoD controls are applied, preventing a single user from both viewing and editing financial information, thereby reducing the risk of fraud.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:**

- **Configure when:** You have a detailed role model in place that utilizes object-level permissions extensively and need to enforce strict SoD controls to comply with regulatory requirements or to enhance internal security policies.
  
- **Avoid when:** Your role model is not finely grained, or the enforcement of SoD at an object-level would lead to unnecessary complexity without significantly enhancing security or compliance postures.