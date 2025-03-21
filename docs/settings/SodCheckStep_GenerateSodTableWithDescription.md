# SoD Check Step Generate SoD Table With Description

**Technical Name:** SodCheckStep_GenerateSodTableWithDescription

**Category:** SOD

**Default Value:** 

**Impact Level:** High

**Description:** This parameter enables the generation of a table with descriptions for Segregation of Duties (SoD) checks within the Pathlock Cloud GRC platform.

**Business Impact:** Enhances the organization's ability to manage and mitigate the risk of fraud and error by providing detailed insights into potential SoD conflicts, thereby strengthening internal controls over financial reporting and operational effectiveness.

**Technical Impact when configured:** Upon configuration, this parameter allows the system to automatically produce and append detailed descriptions to the SoD check table, facilitating more informed decision-making and analysis by providing context and clarity on the nature of identified SoD conflicts.

**Examples Scenario:**

1. During a review of access controls, an auditor requests a report on current SoD conflicts. Enabling this parameter allows the Pathlock Cloud GRC platform to generate a comprehensive table that includes not only the conflicts but also their descriptions, simplifying the auditor's review process.

2. An organization is implementing a new policy to periodically review user rights within their financial systems to prevent fraud. By configuring this parameter, the system automatically produces detailed reports on potential SoD conflicts, aiding in the rapid identification and remediation of issues.

**Related Settings:** 

- PerformWorkflowActionsInBackground
- RoleAdvisorExcludeRolesBusinessProcess

**Best Practices:** Configure when initiating comprehensive SoD audits to enhance transparency and accountability. Avoid when detailed reporting is unnecessary, to streamline workflow and reporting processes.