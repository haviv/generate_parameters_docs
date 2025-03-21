# New Password Forbidden Characters

**Technical Name:** NewPasswordForbiddenCharacters

**Category:** Security

**Default Value:** N/A

**Impact Level:** High

**Description:**

A security parameter in Pathlock Cloud GRC platform that specifies a set of characters which are not allowed to be used in new passwords. This is utilized to enhance password policies by preventing the use of characters that might either introduce security vulnerabilities or are known to cause issues in processing or handling passwords across different systems.

**Business Impact:**

Imposing specific restrictions on password composition enhances the overall security posture of the organization by ensuring that users create passwords that are complex and harder for attackers to guess or breach through brute-force attacks. It also helps standardize password policies across the organization, aligning with best practices in password management.

**Technical Impact when configured:**

When this parameter is configured, any new password created by users or administrators within the system will be subjected to validation checks against the forbidden characters list. Attempting to use any of these restricted characters in a password will result in a password creation error, prompting the user to choose a password that complies with the established policy.

**Examples Scenario:**

- **Given Scenario:** An organization has identified that certain characters (`<`, `>`, `&`, `%`) cause issues when passwords are processed by their legacy systems. 
- **Action:** The organization configures the `NewPasswordForbiddenCharacters` parameter to include these characters.
- **Outcome:** Users are no longer able to create passwords containing `<`, `>`, `&`, `%`, thereby eliminating the identified processing issues and aligning the password policy with organizational security requirements.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:** You need to align with an organizational password policy that restricts specific characters to prevent security issues or processing errors.
- **Avoid when:** There is no clear requirement or justification for excluding specific characters from passwords, as overrestriction can lead to reduced password complexity by limiting the character set available to users.