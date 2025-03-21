# New Username Forbidden Characters

**Technical Name:** NewUsernameForbiddenCharacters

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies characters that are not allowed in usernames within the Pathlock Cloud GRC platform. It is designed to enforce username policies by restricting the use of certain characters that may not be secure or are reserved for specific system functions.

**Business Impact:**

Implementing this parameter directly influences an organization's security posture by preventing the inclusion of potentially harmful characters in usernames. This could mitigate risks associated with injection attacks or other security vulnerabilities that could be exploited via user inputs. Additionally, it ensures consistency and standardization of usernames across the organization's user base.

**Technical Impact: when configured**

When configured, the NewUsernameForbiddenCharacters parameter actively filters out the specified characters from any new usernames created. This ensures compliance with the organization's username policy and enhances overall system integrity and security. It operates by validating new usernames against the forbidden characters list and either rejecting those usernames or requiring modification before acceptance.

**Examples Scenario:**

If an organization decides to exclude special characters such as `*`, `?`, and `&` from usernames to simplify user management and avoid command line interpretation issues, they would configure the NewUsernameForbiddenCharacters parameter accordingly. This policy would help in avoiding complications that might arise from users accidentally or maliciously including such characters in their usernames, potentially leading to system misuse or exploitation.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** configure when establishing or updating the organization's username creation policies to include prohibitions on specific characters. Avoid configuring without a clear understanding of how the forbidden characters might impact user creation workflows or system interoperability.