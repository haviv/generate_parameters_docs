**Technical Name:** FileManagerUploadForbiddenFilenameSequences

**Category:** Security

**Default Value:** exe,asp,php,jsp,rar

**Impact Level:** High

**Description:**

The FileManagerUploadForbiddenFilenameSequences parameter specifies sequences of characters (usually file extensions) that are not allowed in file names for uploads. This setting is designed to prevent the uploading of potentially malicious files that could harm the system or compromise security.

**Business Impact:**

Configuring forbidden filename sequences protects the organization's data and systems from unauthorized access, malware, and other security threats that might arise through the exploitation of file uploads. It ensures that only safe and allowed file types are uploaded, thereby reducing the risk of security breaches.

**Technical Impact when configured:**

When configured, the system will reject any files containing the forbidden filename sequences during the upload process. This acts as a first line of defense against file-based vulnerabilities by ensuring that files with potentially harmful extensions are blocked.

**Examples Scenario:**

An organization wants to prevent the execution of unauthorized scripts on their server. By setting `FileManagerUploadForbiddenFilenameSequences` to include 'php,asp,jsp', they can block uploads of PHP, ASP, and JSP files, which could be used to execute malicious scripts.

**Related Settings:**

- `FileManagerUploadForbiddenFileTypes`

**Best Practices:** configure when, avoid when

- **Configure when:** You have identified specific file types or filename sequences that pose a security risk to your environment. Regularly update this list based on evolving security insights and threat intelligence.
  
- **Avoid when:** Implementing this without understanding the file types your users need to upload can unintentionally hinder legitimate business processes. Ensure that restrictions align with business needs without compromising security.