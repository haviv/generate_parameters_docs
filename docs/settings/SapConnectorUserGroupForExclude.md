# Sap Connector User Group For Exclude

**Technical Name:** SapConnectorUserGroupForExclude

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter is used to specify user groups in SAP that should be excluded from certain operations or analytics within the Pathlock Cloud GRC platform. It helps in refining the scope of security, compliance, or risk management activities by eliminating irrelevant user data.

**Business Impact:** Proper configuration of this parameter can significantly reduce the noise in security, compliance, and risk management reports by excluding user groups that are not relevant to specific audits or checks. This focused approach can lead to more accurate risk assessment and more targeted security measures, ultimately protecting sensitive information and ensuring compliance with regulatory standards.

**Technical Impact when configured:** When configured, actions or checks performed by the Pathlock Cloud GRC platform will ignore users belonging to the specified SAP user groups. This could include skipping these users in access reviews, segregation of duties (SOD) analyses, or risk assessments. As a result, system performance may improve, and reports generated will be more relevant to the user's needs.

**Examples Scenario:** An organization may want to exclude temporary or intern user groups from being analyzed in SOD reports to focus on permanent employees. By doing so, the organization ensures that their critical SOD checks are not diluted with entries that are not of concern, allowing security teams to focus on areas with higher risk.

**Related Settings:** 

- ImpactAnalysisShowControlsFromCombinationOnlyHideMigitaionBoxForOtherRisks 

**Best Practices:** configure when user groups consist of accounts not relevant for your security or compliance posture, such as service accounts or external consultants; avoid when all user groups within SAP are relevant to your GRC activities, to ensure comprehensive coverage.