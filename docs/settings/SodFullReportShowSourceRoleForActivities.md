# SoD Full Report Show Source Role For Activities

**Technical Name:** SodFullReportShowSourceRoleForActivities

**Category:** Reporting

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter controls whether the source roles associated with activities are displayed in the Segregation of Duties (SoD) Full Report within the Pathlock Cloud GRC platform. It is used to enhance the visibility of the roles that contribute to potential SoD violations by including detailed role information directly in the report output.

**Business Impact:**

Enabling the display of source roles for activities in the SoD reports provides a deeper level of insight for auditors and compliance managers into how specific roles contribute to SoD conflicts. This can aid in the identification and remediation of security risks, ensuring that appropriate separation is maintained according to organizational policies and regulatory requirements.

**Technical Impact when configured:**

When enabled, the SoD Full Report will include additional columns or sections that detail the individual roles involved in each activity that has been flagged for potential SoD violations. This facilitates more effective analysis and review processes by pinpointing exactly which roles need adjustments to mitigate risk.

**Examples Scenario:**

- A compliance officer is conducting a review of SoD violations in preparation for an upcoming audit. By activating this parameter, the officer can quickly identify specific roles contributing to violations, enabling targeted remediation efforts.
  
- During internal reviews, a security manager identifies a high number of SoD conflicts within certain business processes. Enabling this parameter helps to break down the conflicts by roles, simplifying the task of redesigning roles for tighter security and compliance.

**Related Settings:** N/A

**Best Practices:** configure when the organization requires detailed analysis and documentation of role-based access controls to meet stringent audit requirements; avoid when unnecessary to reduce report complexity and size.
