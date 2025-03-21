# Sap Connector User Group For Include

**Technical Name:** SapConnectorUserGroupForInclude

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SapConnectorUserGroupForInclude` parameter is used to specify user groups that should be included during the synchronization or processing tasks within the Pathlock Cloud GRC platform, particularly in relation to SAP connectors. This setting allows for granular control over which SAP user groups are considered by the platform, enhancing both security and compliance by focusing on relevant user data.

**Business Impact:**

By properly configuring this parameter, organizations can ensure that their GRC activities, such as risk analysis and compliance checks, are focused on relevant user groups. This targeted inclusion can lead to more efficient GRC processes, by reducing the noise from unrelated user data and streamlining the analysis process. In turn, this can help in sharper, more accurate compliance and security postures specific to critical or sensitive user groups within the SAP environment.

**Technical Impact when configured:**

Upon configuration, the Pathlock platform will filter the user lists pulled from SAP systems to include only the specified user groups. This means that any operations, analysis, or reports generated will be based on data from these groups, enhancing the relevancy and accuracy of security and compliance insights derived.

**Examples Scenario:**

An organization wants to ensure that its audit and compliance checks are focused on high-risk user groups within its SAP systems, such as finance or IT administrators. By setting the `SapConnectorUserGroupForInclude` to include these specific groups, the organization can concentrate its GRC efforts on the most sensitive and critical areas of its business operations.

**Related Settings:**

- SapConnectorUserGroupForExclude

**Best Practices:** 

- **Configure when:** You have specific user groups within your SAP system that are of primary concern for security, compliance, or audit purposes. This allows for focused analysis and reporting on these critical groups.
  
- **Avoid when:** Your GRC processes require broad visibility across all user groups or if the exclusion of any group could lead to missed compliance or security risks. In such cases, it might be better to include all groups or strategically use the exclusion parameter to omit only non-critical groups.