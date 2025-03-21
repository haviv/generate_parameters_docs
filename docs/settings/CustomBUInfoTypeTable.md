# Custom BUInfo Type Table

**Technical Name:** CustomBUInfoTypeTable

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Custom BUInfo Type Table parameter is designed to allow the customization of the Business Unit (BU) information type within the SAP Connector component of the Pathlock Cloud GRC platform. It specifies the table and fields to be used for retrieving relevant Business Unit data, facilitating tailored security, risk, and compliance activities related to Business Units.

**Business Impact:**

Configuring this parameter can enhance the platform's adaptability to the organization’s unique structure by enabling more accurate analysis and reporting of GRC data at the Business Unit level. This customization can lead to improved insights into security, risk, and compliance issues specific to different BUs, allowing for more targeted and effective mitigation strategies.

**Technical Impact when configured:**

Once configured, the Custom BUInfo Type Table impacts how the SAP Connector reads and interprets Business Unit information from SAP systems. It enables the integration of customized Business Unit data into the GRC processes, affecting the accuracy and relevance of security and compliance reporting and analysis.

**Examples Scenario:**

Suppose an organization wants to align its GRC activities with its unique organizational structure, where Business Units are defined by a combination of SAP object types and planning versions not covered by the default settings. By configuring the Custom BUInfo Type Table to match these unique identifiers, the organization can ensure that its GRC reporting and analysis accurately reflect its Business Unit structure, thereby improving the relevancy and actionability of these insights.

**Related Settings:**

- CommonSettings.Default.CustomBUTypeObjectType

**Best Practices:** configure when you need to adapt the GRC processes to a customized Business Unit structure not adequately covered by default settings; avoid when the default SAP Connector configuration meets the organization's needs for Business Unit analysis and reporting.
