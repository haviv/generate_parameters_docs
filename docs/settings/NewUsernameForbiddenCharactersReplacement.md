# New Username Forbidden Characters Replacement

**Technical Name:** NewUsernameForbiddenCharactersReplacement

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to specify how forbidden characters in new usernames should be replaced during the user creation process in the Pathlock Cloud GRC platform. The setting ensures that usernames adhere to specified compliance and security standards by eliminating or substituting characters that are not allowed.

**Business Impact:**

Incorrect or unsafe characters in usernames can pose security risks and compliance issues. For example, certain symbols might be used in scripting attacks or could cause errors in system processes that rely on username format consistency. Ensuring usernames do not contain forbidden characters helps maintain system integrity and security posture.

**Technical Impact when configured:**

When this parameter is configured, it automatically modifies new usernames to remove or replace characters defined as forbidden. This process occurs as part of the user creation service, ensuring all new usernames comply with security policies before being committed to the system. It helps in streamlining user management and reduces the administrative overhead involved in manually correcting username formats.

**Examples Scenario:**

An organization specifies that usernames should not contain punctuation marks to simplify user management and avoid coding errors in scripts that interact with usernames. By setting this parameter, any new usernames created with forbidden characters, such as periods or commas, will have those characters replaced according to the policy specified by the parameter.

**Related Settings:**

- `AllowEditWorkflowFormRole`

**Best Practices:** 

- **Configure when:** Prelude setting up user creation policies to ensure all usernames comply with organizational security standards.
- **Avoid when:** Custom handling of forbidden characters is preferred or if there’s a specific need to allow characters that are generally forbidden.