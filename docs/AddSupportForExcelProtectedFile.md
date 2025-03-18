# Add Support For Excel Protected File

**Technical Name:** AddSupportForExcelProtectedFile

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter enables the Pathlock Cloud GRC platform to handle and process Excel files that are protected by passwords or encryption. When enabled, users can upload, analyze, and report on data contained in protected Excel documents as part of their governance, risk, and compliance activities.

**Business Impact:**

Enabling support for Excel protected files will allow organizations to ensure that sensitive data contained within protected spreadsheets can be securely managed and included in compliance and audit reporting. This is particularly important for businesses that regularly deal with confidential financial, personnel, or operational data in Excel format.

**Technical Impact: when configured**

Upon configuration, the system will have the capability to ingest, decrypt, and process Excel files that are protected. This means that workflows which involve the uploading or analysis of Excel documents will be able to accept files that were previously inaccessible due to protection.

**Examples Scenario:**

A financial analyst needs to upload an annual budget report housed in a password-protected Excel file to the Pathlock Cloud GRC platform for audit trail purposes and compliance review. With the AddSupportForExcelProtectedFile parameter enabled, they can upload this document directly without having to remove the password protection, thus maintaining the security of sensitive financial data.

**Related Settings:**

- ShowRoleOwnersInRoleQuery

**Best Practices:** Enable this setting when dealing with sensitive data within protected Excel files that need to be included in GRC processes. Avoid enabling it if your organization rarely encounters protected Excel documents in governance, risk, and compliance activities, to minimize unnecessary processing overhead.