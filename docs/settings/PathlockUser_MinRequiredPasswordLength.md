# Pathlock User Min Required Password Length

**Technical Name:** PathlockUser_MinRequiredPasswordLength

**Category:** Security

**Default Value:** 1

**Impact Level:** High

**Description:**

This parameter specifies the minimum number of non-alphanumeric characters that must be present in a user's password within the Pathlock Cloud GRC platform. Ensuring passwords contain non-alphanumeric characters enhances security by making passwords more complex and difficult to guess or crack.

**Business Impact:**

Adequate password complexity is critical for safeguarding sensitive business data and access controls within an organization. By enforcing a minimum number of non-alphanumeric characters in passwords, organizations can prevent unauthorized access, thereby protecting against potential data breaches and ensuring compliance with various regulatory standards.

**Technical Impact when configured:**

When this parameter is configured to enforce a minimum amount of non-alphanumeric characters, it directly impacts user account security. It forces users to create passwords with increased complexity, significantly enhancing the overall security posture by reducing the risk of password-related breaches.

**Example Scenario:**

*Scenario:* An organization needs to comply with industry standards that require robust password policies to protect sensitive data.

*Application:* By setting the `PathlockUser_MinRequiredPasswordLength` parameter to a higher value, the organization ensures all user passwords contain a minimum number of non-alphanumeric characters, aligning with best security practices and compliance requirements.

**Related Settings:**

- PathlockUser_MinRequiredNonAlphanumericCharacters

**Best Practices:** 

- **Configure when:** You are establishing or updating your organization's password policy to enhance security and meet compliance requirements.
  
- **Avoid when:** Lower security requirements are acceptable due to the nature of the protected data or system. However, always consider the broader implications of security settings in the context of your overall risk management strategy.