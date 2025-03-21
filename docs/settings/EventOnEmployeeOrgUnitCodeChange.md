# Event On Employee Org Unit Code Change

**Technical Name:** EventOnEmployeeOrgUnitCodeChange

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:** Toggle to enable or disable event monitoring for changes to an employee's organizational unit code. This feature is aimed at tracking adjustments in employee departmental alignments or positions within the organizational structure.

**Business Impact:** Keeping track of changes to employee organizational units is essential for maintaining up-to-date access control and ensuring compliance with internal policies and external regulations. It helps prevent unauthorized access stemming from outdated employee role information.

**Technical Impact when configured:** When enabled, the system initiates monitoring and logging of changes to an employee’s organizational unit code, potentially triggering workflow actions or notifications based on the configured parameters. This facilitates real-time oversight and auditing of critical HR data changes.

**Example Scenario:** An employee is transferred from the marketing to the sales department, and their organizational unit code changes accordingly. Enabling this parameter ensures that the transition is monitored and logged, triggering any associated workflows for access adjustments or compliance assessments.

**Related Settings:** SoDImpactAnalysisCalculator_ExcludeSensitiveAccess

**Best Practices:** Configure this parameter to monitor changes in employee organizational unit codes in environments where role-based access control is critical for maintaining security and compliance. Avoid enabling this feature in cases where frequent, routine changes in organizational structure occur, leading to unnecessary alerts or workflow triggers.