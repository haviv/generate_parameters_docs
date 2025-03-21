**Technical Name:** WB2_V_MKPF_MSEG2_Fields

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The WB2_V_MKPF_MSEG2_Fields parameter is designed to configure the SAP connector within the Pathlock Cloud GRC platform. It primarily influences how transaction data, specifically related to change documents, are read and processed from the SAP system. This setting allows users to fine-tune which change document types are actively monitored and included in compliance reporting.

**Business Impact:**

Configuring WB2_V_MKPF_MSEG2_Fields correctly ensures that only relevant transactional data is captured and analyzed for compliance reporting. This focused data collection helps organizations avoid information overload and concentrate on high-risk activities, thereby maintaining a robust security and compliance stance. Effective configuration of this parameter plays a crucial role in risk management, audit trails, and the overall integrity of GRC reporting.

**Technical Impact when configured:**

- Optimizes the performance of the SAP connector by filtering out unnecessary data.
- Ensures accurate and relevant compliance reporting by monitoring specific change document types.
- Enhances the effectiveness of security and compliance audits by providing a clear, auditable trail of high-priority transactional changes.

**Examples Scenario:**

An organization needs to monitor transactions for potential segregation of duties (SoD) violations within their financial system. By configuring WB2_V_MKPF_MSEG2_Fields to include only financial document changes, the Pathlock platform can more efficiently identify and alert on relevant activities that may indicate SoD issues.

**Related Settings:**

- EnableCUA
- CheckActivityModeForHighRiskActivityEvent

**Best Practices:** 

- Configure when: Your organization requires detailed monitoring of specific SAP transaction types for compliance and security purposes.
- Avoid when: Broad, non-specific monitoring is sufficient for your compliance and security needs, or system performance is a concern.