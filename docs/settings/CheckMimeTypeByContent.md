# Check Mime Type By Content

**Technical Name:** CheckMimeTypeByContent

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:** This parameter ensures that uploaded files' MIME types are validated based on their content, enhancing the platform's defense against potential security risks from malicious file uploads.

**Business Impact:** Proper configuration of this parameter helps prevent the upload of potentially dangerous file types which may appear harmless by their extension but are identified as harmful through their content, thus safeguarding sensitive data and compliance-related information.

**Technical Impact when configured:** When enabled, this feature cross-references a file's MIME type with a list of forbidden types based on its actual content rather than its extension, significantly reducing the risk of executing or storing harmful files within the system.

**Examples Scenario:** If an attacker attempts to upload a malicious script disguised with a .txt extension, this feature will analyze the content of the file and block the upload if it detects script-like characteristics, despite the misleading extension.

**Related Settings:** WorkflowUploadForbiddenFileTypes

**Best Practices:** Configure this parameter to be always enabled to ensure the highest level of security. Avoid disabling this feature, as doing so might leave the system vulnerable to uploads of files with malicious content.
