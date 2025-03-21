# Allowed Upload File Types

**Technical Name:** AllowedUploadFileTypes

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**
The Allowed Upload File Types parameter controls which file types are permitted for upload on the Pathlock Cloud GRC platform. It aims to enhance security by filtering out potentially harmful file types that could be used in cyber attacks.

**Business Impact:**
Setting up a strict policy for file uploads greatly reduces the risk of security breaches. Allowing only necessary file types ensures that the platform is not easily compromised by malicious files, thereby protecting sensitive compliance and risk management data.

**Technical Impact when configured:**
When properly configured, this parameter ensures that only files with extensions deemed safe are allowed to be uploaded. This significantly lowers the risk of uploading files that could contain malware or other harmful entities designed to exploit system vulnerabilities.

**Examples Scenario:**
- **Scenario 1:** An organization decides to only allow PDF and Excel files (.pdf, .xlsx) to be uploaded for reporting purposes, thereby preventing the upload of executable (.exe) files, which could be harmful.

**Related Settings:**
- ValidateByFileTypeBlackList

**Best Practices:** 
- **Configure when:** You are setting up the system for the first time or updating security protocols. It's crucial to allow only the necessary file types specific to your organization's operational requirements.
- **Avoid when:** There is a lack of clarity on which file types are essential for your organization's operational needs. In such cases, consult with your IT security team to define a comprehensive list of safe file types before configuring this parameter.