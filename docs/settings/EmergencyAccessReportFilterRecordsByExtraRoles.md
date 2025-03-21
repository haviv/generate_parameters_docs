# Emergency Access Report Filter Records By Extra Roles

**Technical Name:** EmergencyAccessReportFilterRecordsByExtraRoles

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

This parameter is designed to filter records in the Emergency Access Activity Log based on additional roles that are not directly assigned to the user. It enhances the security by allowing administrators to perform in-depth audits and oversight on emergency access by including roles that extend beyond the user’s regular permission set.

**Business Impact:**

Applying this filter can significantly enhance the organization's security posture by providing detailed insights into emergency access usage, including roles that may grant extensive system privileges. It helps in identifying potential misuse of emergency access privileges or detecting security loopholes.

**Technical Impact when configured:**

When enabled, this setting filters the activity log to include records associated with extra roles assumed during emergency access sessions. This ensures that any actions taken under these additional roles are subject to scrutiny, aiding in compliance and forensic analysis.

**Examples Scenario:**

A user is granted emergency access to perform certain operations in the system under a high-privileged role that is not part of their standard role assignment. With this parameter enabled, the Emergency Access Activity Log will include activities performed under these extra roles, making it possible to audit actions that could impact system security or data integrity.

**Related Settings:**

- DisableInitLastUseOfActivity

**Best Practices:** 

- **Configure when:** Regular monitoring and auditing of emergency access including extra roles are a compliance requirement or when there is a need to enhance security oversight over privileged access.
  
- **Avoid when:** The detailed audit of actions performed under emergency roles might result in an overwhelming amount of data with no added security value, or if it impacts system performance due to the high volume of logs generated.