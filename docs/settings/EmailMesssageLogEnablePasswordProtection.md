# Email Message Log Enable Password Protection

**Technical Name:** EmailMesssageLogEnablePasswordProtection

**Category:** Security

**Default Value:** Not specified

**Impact Level:** High

**Description:**

This parameter controls the password protection feature for email message logs in the Pathlock Cloud GRC platform. When enabled, it ensures that access to email logs is secured and requires authentication, enhancing the security of sensitive information contained within these logs.

**Business Impact:**

Enabling password protection for email message logs helps to prevent unauthorized access to sensitive information, such as user actions and system alerts, conveyed through email communications. This is crucial for maintaining confidentiality and integrity of the information, thereby supporting compliance with various regulations on data protection and privacy.

**Technical Impact when configured:**

Once configured, any attempt to access the email message logs will require authentication. This adds an additional layer of security, ensuring that only authorized personnel can view the logs, thereby safeguarding sensitive information against external breaches or insider threats.

**Examples Scenario:**

A scenario where this parameter would be particularly beneficial is in a highly regulated industry, such as finance or healthcare, where email communications might contain sensitive information about transactions or patient data. Enabling password protection ensures that even if an unauthorized party gains access to the system, the email logs remain secure and inaccessible without the proper credentials.

**Related Settings:**

- DnsPostfixForDisableWindowsAuthentication
- ActiveDirectoryEmployeeIDAttribute

**Best Practices:** configure when handling sensitive or regulated data through emails; avoid when there is no sensitive information communicated through email logs or in environments where access controls and monitoring are already exceptionally stringent, reducing the need for additional password protection layers.