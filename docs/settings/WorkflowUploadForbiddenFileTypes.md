# Workflow Upload Forbidden File Types

**Technical Name:** WorkflowUploadForbiddenFileTypes

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:** 

This parameter defines a list of file types that are not allowed to be uploaded within workflow processes. It aims to prevent unauthorized or potentially harmful files from being introduced into the system, ensuring a secure management of files in compliance with organizational policies.

**Business Impact:** 

Implementing restrictions on uploadable file types mitigates the risk of security breaches that could lead to data loss, data theft, or the spread of malware. It safeguards sensitive information from being exposed or compromised and ensures that the system remains in compliance with relevant data protection regulations.

**Technical Impact when configured:**

Once configured, the system will reject any attempts to upload files that match the forbidden file types during workflow processes. This adds an important layer of security by automatically enforcing file management policies and limiting the opportunity for malicious files to enter the system or sensitive information to be inappropriately distributed.

**Examples Scenario:**

To prevent the potential risk of macro-enabled documents executing unauthorized commands, an organization configures the WorkflowUploadForbiddenFileTypes to include .docm and .xlsm file types. As a result, users are unable to upload these types of documents within any workflow processes, thereby reducing the risk of a security vulnerability being exploited.

**Related Settings:** 

While specific related settings were not explicitly listed in the provided code references, the parameter works in conjunction with other file validation and security settings within the platform to comprehensively protect the integrity and security of the system.

**Best Practices:** 

- **Configure when:** There is a need to adhere to security policies that specify restrictions on certain file types due to their potential risks or lack of relevance to business processes.
- **Avoid when:** If the restriction overly complicates legitimate business processes or if all file types can be securely managed through other controls.