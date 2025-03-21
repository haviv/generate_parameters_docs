# Number of days before 'end date' for default 'start date'

**Technical Name:** StartDateDaysBack

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to define the default number of days to look back from the current date (or a specified 'end date') when generating reports in the Pathlock Cloud GRC platform. It helps in setting a dynamic 'start date' for reporting purposes, facilitating temporal analysis of data over a specific duration leading up to the present or a chosen end point.

**Business Impact:**

Adjusting this parameter allows businesses to tailor the temporal scope of their security, risk, and compliance reports. By controlling the period under review, organizations can better monitor trends, identify patterns, and address issues relevant to their GRC (Governance, Risk Management, and Compliance) processes. This flexibility is crucial for maintaining robust security postures, ensuring compliance, and managing risks effectively.

**Technical Impact when configured:**

Configuring `StartDateDaysBack` affects the volume and specificity of data included in reports. A shorter timeframe may lead to overlooking longer-term trends, while a longer timeframe can provide a more comprehensive view but might include outdated or irrelevant data. Proper configuration aligns report outputs with business needs, ensuring decision-makers have access to timely, relevant, and actionable insights.

**Examples Scenario:**

- **Audit Preparation:** An organization sets `StartDateDaysBack` to 90 days to prepare for a quarterly audit, ensuring the report captures all relevant events and changes within the audit period.
  
- **Risk Assessment:** To assess risks following a significant policy update, `StartDateDaysBack` is set to 30 days, focusing the report on immediate post-implementation impacts.

**Related Settings:**

- `ShowTransactionAttributesOnReports`: Toggles the inclusion of transaction attributes in reports, which may be relevant when analyzing data over the period defined by `StartDateDaysBack`.
  
- `SodResolverConfig_UseDerivedRoles`: This setting might influence the scope of roles considered in SoD (Separation of Duties) reports, interacting with the period defined by `StartDateDaysBack`.

**Best Practices:** 

- **Configure when:** Preparing for specific audits or compliance checks that require data from a precise timeframe.
  
- **Avoid when:** Continuous, real-time monitoring is required, as the parameter is designed for retrospective reporting over defined periods.