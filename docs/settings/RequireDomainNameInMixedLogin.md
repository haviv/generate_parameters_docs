# Require Domain Name In Mixed Login

**Technical Name:** RequireDomainNameInMixedLogin

**Category:** User Management

**Default Value:** ""

**Impact Level:** Medium

**Description:**

This parameter dictates whether a domain name is required when using a mixed-login method. This is specifically applicable in environments where both Windows authentication and another form of login are permitted.

**Business Impact:**

The enforcement of a domain name in mixed logins can enhance security by ensuring that user credentials are scoped correctly to their respective domains, reducing the risk of unauthorized access due to username conflicts or impersonation within multi-domain environments. It also aids in user management by providing clarity on the user's origin.

**Technical Impact when configured:**

When enabled, users must include their domain name when logging in using mixed mode. This adds an additional layer of verification to the login process, ensuring users are authenticated against the correct domain. Failure to provide the domain name will result in login errors or denied access.

**Examples Scenario:**

- **Scenario 1:** A corporation with multiple domains allows users from any domain to access the Pathlock GRC platform. To ensure that users log in under the correct credentials and domain, the RequireDomainNameInMixedLogin parameter is enforced. This ensures that JohnDoe from DomainA does not inadvertently or maliciously access DomainB resources.
  
- **Scenario 2:** During an audit, it's discovered that users often forget to specify their domain when logging in, leading to repeated failed login attempts and support tickets. Implementing RequireDomainNameInMixedLogin prompts users to remember to include their domain, reducing support inquiries and improving user login efficiency.

**Related Settings:**

- MixedWindowsSecondaryDomainName

**Best Practices:** 

- **Configure when:** Multiple domains exist within the organization and there's a need to differentiate users distinctly by their domain at the login stage.
- **Avoid when:** The organization uses a single domain or when the login process is designed to be domain-agnostic.