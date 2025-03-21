**Technical Name: WB2_V_RBKP_RSEG2_Fields**

**Category: Configuration**

**Default Value:** *Not provided in code references*

**Impact Level: Medium**

**Description:**

The `WB2_V_RBKP_RSEG2_Fields` parameter is used to configure specific SAP connector settings within the Pathlock Cloud GRC platform. This parameter likely influences how data is extracted from SAP, affecting change document readers and potentially other aspects of data handling.

**Business Impact:**

Adjusting this parameter could impact the accuracy and completeness of data imported into Pathlock Cloud GRC from SAP systems. It may affect compliance reporting, risk assessments, and security audits by altering the scope or detail of extracted data.

**Technical Impact when configured:**

Configuring `WB2_V_RBKP_RSEG2_Fields` can enhance or restrict the range of data collected by SAP connectors. Proper configuration ensures that relevant data for compliance, risk management, and security monitoring is accurately captured and processed.

**Examples Scenario:**

A compliance officer needs to ensure that all relevant purchase order changes are tracked within the GRC platform for auditing purposes. By correctly setting the `WB2_V_RBKP_RSEG2_Fields`, they can include necessary fields related to purchase order alterations to meet compliance requirements.

**Related Settings:**

- `BlockSizeForMatrixQuery`
- `EnableCUA`

**Best Practices:** configure when you need to adjust the scope of data collection to meet specific compliance or audit requirements; avoid when default SAP connector settings satisfactorily cover your GRC data needs.