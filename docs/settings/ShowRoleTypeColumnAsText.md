**Show Role Type Column As Text**

**Technical Name:** ShowRoleTypeColumnAsText

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the role type column within reports is shown as textual descriptions. When enabled, roles designated as 'Critical' are displayed with a distinct label, enhancing the readability and understanding of role significance within the report data.

**Business Impact:**

Enabling this feature aids organizational leaders and compliance officers in quickly identifying critical roles within the system, simplifying risk assessment and management processes related to user roles and permissions. It directly influences the efficiency of auditing processes and compliance reporting.

**Technical Impact when configured:**

Upon enabling, critical roles are expressly marked with labels within reports, making them easily distinguishable. This adjustment can lead to improved report usability and aids in the faster identification of potential security or compliance concerns related to specific roles.

**Examples Scenario:**

An organization conducts a periodic review of user access rights and roles as part of their internal compliance checks. By enabling this parameter, the compliance team can more easily identify critical roles within the generated reports, facilitating a smoother and more focused review process.

**Related Settings:**

- EnableSystemSelectionNarrowByAssignedRoles

**Best Practices:** configure when 

- Detailed role analysis and reporting are required.
- There is a need to highlight critical roles within the organizational structure in reports.

avoid when

- Simplified reporting is preferred, and the distinction between role types is not necessary.