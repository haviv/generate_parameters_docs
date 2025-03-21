# Sap Erp Version

**Technical Name:** SAPErpVersion

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

The SAPErpVersion parameter is crucial for configuring the Pathlock Cloud GRC platform to accurately align with the specific version of SAP ERP in use. This ensures that all security, risk, and compliance (GRC) features provided by Pathlock are compatible and optimized for the organization's SAP environment.

**Business Impact:**

Selecting the correct SAP ERP version is essential for maintaining the integrity of the GRC processes within the organization. It affects how the platform interprets data and enforces policies, potentially impacting compliance postures, audit readiness, and the overall security strategy.

**Technical Impact when configured:**

Proper configuration impacts the platform's ability to accurately monitor transactions, assess risks, and enforce segregation of duties (SOD) within the SAP ERP environment. This can include the refinement of alerts, reports, and compliance checks to match the operational nuances of the selected SAP ERP version.

**Examples Scenario:**

- An organization undergoing an upgrade from SAP ERP ECC 6.0 to SAP S/4HANA needs to adjust the SAPErpVersion parameter to ensure that their GRC controls and monitoring activities remain effective post-upgrade.
- A new Pathlock Cloud GRC platform implementation where the specific SAP ERP version dictates initial configuration settings to tailor security and compliance checks accurately.

**Related Settings:** 

- CommonSettings.Default.IsValidateInstallation
- CommonSettings.Default.ShowCSG

**Best Practices:**  

- **Configure when:** Initiating the Pathlock platform for the first time or upon upgrading to a new SAP ERP version.
- **Avoid when:** Information about the exact SAP ERP version in use is unclear or when the organization is in the process of changing versions.