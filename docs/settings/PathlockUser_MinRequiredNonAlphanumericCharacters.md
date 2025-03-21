# Pathlock User Min Required Non Alphanumeric Characters

**Technical Name:** PathlockUser_MinRequiredNonAlphanumericCharacters

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

Specifies the minimum number of non-alphanumeric characters (symbols) that must be included in a password for user accounts in the Pathlock Cloud GRC platform. This setting is part of the platform's password complexity requirements to enhance security.

**Business Impact:**

Enforcing a minimum number of non-alphanumeric characters in passwords helps to prevent unauthorized access by making passwords harder to guess or crack. It supports compliance with security policies and regulatory standards that require robust password policies, thereby reducing the risk of data breaches and enhancing the overall security posture of the organization.

**Technical Impact when configured:**

When this parameter is configured, the Pathlock Cloud GRC system will validate that passwords created or updated by users contain at least the specified number of non-alphanumeric characters. If a user's password does not meet this requirement, the system will reject the password and prompt the user to choose a new one that complies with the policy. This ensures that all user accounts have a baseline level of password complexity.

**Examples Scenario:**

- **Compliance Requirement:** An organization must adhere to a regulatory standard that mandates passwords to contain at least one symbol. By setting `PathlockUser_MinRequiredNonAlphanumericCharacters` to `1` or higher, the organization can ensure compliance with this requirement.
- **Enhanced Security Posture:** To strengthen security, an organization decides to require two symbols in all user passwords. The administrator sets `PathlockUser_MinRequiredNonAlphanumericCharacters` to `2`, thereby enhancing the resilience of passwords against brute force attacks.

**Related Settings:** 

- Password Maximum Age Setting
- Password Minimum Age Setting
- Password Must Not Contain Username Setting

**Best Practices:** 
- **Configure when** you need to align with specific security policies or regulatory requirements that specify password complexity, or to enhance the security of user account access.
- **Avoid when** overly strict requirements could lead to user frustration or an increase in password reset requests, unless such requirements are justified by compliance or security needs. Consider balancing security with usability based on the sensitivity of the information being protected.