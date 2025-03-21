# Report Filter Use Wide User Filter

**Technical Name:** ReportFilterUseWideUserFilter

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** Determines whether the report filter should apply a wide user filter, affecting the scope of users included in the report generation process.

**Business Impact:** Configuring this parameter to true broadens the user scope within reports, ensuring comprehensive visibility over user activities and access permissions across the system. It aids in enhanced security oversight and compliance monitoring by providing a thorough review of user engagements and potential risks within the system.

**Technical Impact when configured:** When set to true, the system will include a broader array of user accounts in report analyses, which may result in longer processing times for generating reports due to the increased data volume. Conversely, setting this parameter to false limits the user scope, potentially leading to faster report generation but at the risk of omitting critical user access and activity details.

**Examples Scenario:** An audit requires a comprehensive overview of all user activities and permissions within a certain timeframe. Setting the `ReportFilterUseWideUserFilter` to true ensures the inclusion of all user data in the generated reports, facilitating a thorough audit trail review and aiding in compliance and risk management.

**Related Settings:** 
- ReportFilterUseWideActivityFilter

**Best Practices:** 
- **Configure when:** A thorough analysis of user activities and permissions is necessary, especially in preparation for audits or for comprehensive risk and compliance management.
- **Avoid when:** Report performance is a critical factor and the additional detail on user access is not required.