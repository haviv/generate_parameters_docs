# Not Allowed Characters Upload File

**Technical Name:** NotAllowedChractersUploadFile 

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

This setting specifies the characters that are not permitted in the names of files uploaded to the Pathlock Cloud GRC platform. Ensuring that file names comply with this restriction helps prevent upload of potentially malicious files that could exploit vulnerabilities related to file parsing or handling.

**Business Impact:**

Disallowing specific characters in file uploads helps protect the organization's data and the integrity of the Pathlock Cloud GRC platform by reducing the risk of security breaches through file uploads. It minimizes the possibility of uploading files with names designed to execute malicious code or cause disruption in the system.

**Technical Impact when configured:**

When configured, this parameter actively blocks the upload of files containing any of the specified characters in their names. This serves as a preventative security measure, ensuring that only files with compliant names are allowed, thereby mitigating potential threats.

**Examples Scenario:**

- An end user attempts to upload a script file with an unconventional extension or character in its file name, like `exploit<script>.txt`, which could bypass naive file validation mechanisms. If `<` and `>` are listed as not allowed, the upload of this file is blocked.
- Uploading a file named `config.dll` when `.dll` is disallowed to prevent execution or loading of dynamic-link library files, which could potentially contain harmful code.

**Related Settings:**

No related settings found in the provided code references.

**Best Practices:** 

- **Configure when:** setting up the system for the first time or when revising security policies to include restrictions on file uploads based on the latest threat intelligence.
- **Avoid when:** such restrictions are not compatible with the operational requirements of the organization, but ensure alternative security measures are in place.