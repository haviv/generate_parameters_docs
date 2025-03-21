**Technical Name: ShowUsageMoreInfoField**

**Category: Reporting**

**Default Value:**

**Impact Level: Medium**

**Description:**

This parameter controls the display of additional information fields related to the usage of approved emergency access within the reporting interface. When enabled, users can view detailed insights tied to workflow identifiers, requesters, and descriptions directly from the reporting columns.

**Business Impact:**

Enabling this feature enhances transparency and oversight for administrators and compliance officers by providing immediate access to critical data points. This information can be pivotal during audits, reviews, or when tracking the usage of emergency access permissions, thereby supporting compliance with internal policies and regulatory standards.

**Technical Impact when configured:**

Once activated, this setting adjusts the data presented in the reports by including fields that offer more insight into the approved emergency access events. This ensures that reports generated will contain enriched information, facilitating better decision-making and monitoring.

**Examples Scenario:**

In a scenario where an organization needs to audit the use of emergency access rights, enabling the ShowUsageMoreInfoField parameter would allow auditors to easily access and review detailed information regarding who requested access, when, and for what purpose, directly from the reporting dashboard. This could prove crucial for quickly identifying any misuse of access rights or to ensure compliance with access control policies.

**Related Settings:**

- `EnableApprovedEmergencyAccess`
- `DisableApprovedEmergencyAccess`

**Best Practices:** 

- **Configure when:** there is a need for enhanced transparency and detail in reporting on emergency access usage, especially for organizations with rigorous audit requirements or those that handle sensitive data.
  
- **Avoid when:** minimal reporting suffices, or in environments where the increase in report detail could overwhelm administrators or systems due to the extensive volume of emergency accesses.