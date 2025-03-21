**Enable Include Risk Description Column Activities Matrix Reports**

**Technical Name:** EnableIncludeRiskDescriptionColumnActivitiesMatrixReports

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** 

Enables the inclusion of a risk description column in Activities Matrix Reports exported to Excel. This setting will augment exported reports with detailed risk descriptions, providing users with richer contextual insights relating to the security, risk, and compliance postures of their activities.

**Business Impact:** 

Including a risk description column in Activities Matrix Reports enhances the decision-making process for IT and security teams by providing clear and actionable insights into potential risks associated with various activities within the system. It supports improved audit and compliance practices by facilitating a better understanding of where focus and remediation efforts should be directed.

**Technical Impact when configured:** 

When this parameter is enabled, Activities Matrix Reports generated and exported from the Pathlock platform will include an additional column, detailing risk descriptions for each activity. This enriches the report and serves as a valuable tool for risk assessment and mitigation planning.

**Examples Scenario:** 

A compliance officer exports the Activities Matrix Report to review the access rights and associated risks within their ERP system. By enabling this parameter, the report includes detailed descriptions of risks next to each activity, allowing the officer to quickly identify high-risk activities and prioritize their review and mitigation strategies accordingly.

**Related Settings:** 

- `DailyEMailAddLinkToWaitingRequests`
- `CustomRoleForUsage`
- `EnableExcelMatrixTextRotation`

**Best Practices:** 

- **Configure when:** Detailed risk analysis and documentation are required for audit purposes, or to enhance the understanding and management of security postures within your GRC framework.
  
- **Avoid when:** Minimal reporting is sufficient, or in scenarios where report simplicity is prioritized over detailed insights.