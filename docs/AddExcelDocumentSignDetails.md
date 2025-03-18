**Add Excel Document Sign Details**

**Technical Name:** AddExcelDocumentSignDetails

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AddExcelDocumentSignDetails` parameter controls the inclusion of signature details in exported Excel documents within the Pathlock Cloud GRC platform. When enabled, this feature ensures that Excel reports generated from the platform include an additional layer of detail relevant to audit trails and document verification processes.

**Business Impact:**

Enabling this parameter ensures that Excel documents produced by the system carry detailed information regarding the document's creation, modification, and approval processes. This is crucial for compliance, auditability, and for maintaining a transparent and verifiable record of actions taken on sensitive data.

**Technical Impact when configured:**

When this parameter is configured to include signature details, each Excel document generated will include metadata or visible elements detailing the document's signatory information. This might extend the document generation time slightly but ensures that documents meet compliance and audit requirements.

**Examples Scenario:**

- **Audit Preparation:** An organization is preparing for an internal or external audit and requires that all exported reports contain comprehensive details on who generated the report, when it was generated, and if applicable, who approved its contents.
- **Compliance Documentation:** A company operates in a highly regulated industry where it must prove that data exports are controlled and verified. Enabling this parameter allows the organization to automatically include this verification in every Excel report output.

**Related Settings:**

- `DisableHeader`: Controls whether headers are included in exported Excel documents.

**Best Practices:** 

- **Configure when:** Preparing reports for audit trail purposes or when needing to meet strict compliance requirements related to document verification and signatory details.
- **Avoid when:** Quick, informal reports are needed without the overhead of additional processing time or where signatory details are irrelevant.