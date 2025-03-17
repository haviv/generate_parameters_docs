# Add Support For Excel Protected File

**Technical Name:** AddSupportForExcelProtectedFile

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter enables the Pathlock platform to handle Excel files that are protected. When enabled, it allows users to upload, download, and work with Excel files that have been protected with a password. This is particularly useful for organizations that use Excel documents for reporting, data transfer, or record-keeping but need to maintain confidentiality and data integrity.

**Business Impact:** Enabling support for protected Excel files ensures that sensitive data contained within these files remains secure while being processed or analyzed through the Pathlock platform. It supports compliance with data protection regulations by ensuring that only authorized personnel can access or modify the protected files. This feature is crucial for businesses that rely on Excel for critical financial analysis, risk assessment, or compliance reporting.

**Technical Impact:** When configured, the Pathlock platform will prompt for passwords to access protected Excel files, or it will use stored credentials securely. This ensures that all file interactions—be it data import/export or other batch processing tasks—are conducted securely without compromising the file's integrity or accessibility by unauthorized users.

**Example Scenario:**
- **Scenario:** A financial analyst needs to upload a series of password-protected Excel files containing sensitive budget information for processing within the Pathlock platform.
- **Requirement:** The AddSupportForExcelProtectedFile parameter must be enabled to allow the analyst to upload and work with the protected files seamlessly.
- **Outcome:** With the parameter enabled, the analyst uploads the protected Excel files, the platform prompts for the necessary passwords, and the data is processed securely, maintaining the confidentiality of the information.

**Related Settings:** 
- ExcelFileProcessingMode (determines how Excel files are processed, which may relate to how protected files are handled once this parameter is enabled)
- SecureCredentialStorage (controls how passwords or credentials for accessing protected files are stored and managed within the platform)

**Applicable Workflow Actions:** 
- ImportData
- ExportData
- AnalyzeData

**Best Practices:** 
- **Configure When:** Handling of protected Excel files is a regular part of your data processing or reporting workflows, and the security of the contained data is paramount.
- **Avoid When:** Your organization does not use Excel for sensitive information, or there are no requirements to interact with password-protected files, to minimize complexity.

**Context:** This parameter is crucial for businesses that manage sensitive data within Excel documents, ensuring that security and data integrity are maintained across GRC (Governance, Risk Management, and Compliance) initiatives within the Pathlock Cloud platform.