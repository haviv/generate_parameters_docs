# Custom Domains Split By

**Technical Name:** CustomDomainsSplitBy

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CustomDomainsSplitBy` parameter is designed for specifying the character or sequence used to split domain names in configurations related to the integration of Pathlock Cloud GRC with Active Directory (AD). It determines how domain names in a list are separated, playing a crucial role in the correct parsing and application of domain settings across the platform.

**Business Impact:**

Correct configuration of this parameter ensures that users are properly authenticated against their respective domains, facilitating secure and efficient access control and identity management. Misconfiguration may lead to authentication issues, impacting user experience and potentially compromising security.

**Technical Impact: when configured**

When properly configured, the system can accurately distinguish between multiple domain names provided in settings, allowing it to authenticate users against the correct domain in multi-domain environments. This enhances the platform's ability to manage user access across diverse organizational structures seamlessly.

**Examples Scenario:**

For instance, if your organization operates with multiple domains for different departments or geographic locations (e.g., "us.example.com" and "eu.example.com"), setting `CustomDomainsSplitBy` to a semicolon (`;`) enables the system to effectively recognize and apply unique domain settings for authentication purposes: `us.example.com;eu.example.com`.

**Related Settings:**

- `CommonSettingsParameters`

**Best Practices:** configure when setting up or modifying Active Directory integrations to ensure domains are recognized correctly; avoid when not using multiple domains or if the default splitting character meets organizational requirements.