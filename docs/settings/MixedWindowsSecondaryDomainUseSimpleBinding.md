# Mixed Windows Secondary Domain Use Simple Binding

**Technical Name:** MixedWindowsSecondaryDomainUseSimpleBinding

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter configures the authentication method for secondary domains in a mixed Windows environment. It specifies whether to use simple binding for verifying passwords in secondary domains.

**Business Impact:**

Enabling simple binding can streamline the authentication process, potentially improving system access times for users in secondary domains. However, it might also reduce security by simplifying the authentication mechanism, depending on the network configuration and security requirements.

**Technical Impact when configured:**

- If enabled (set to True), authentication for users logging into the Pathlock GRC platform from secondary domains will use a less complex, potentially less secure method.
- If disabled (remains False), the system will use a more secure, complex method for authenticating these users.

**Examples Scenario:**

- A company uses Pathlock GRC for compliance and risk management across their primary and multiple secondary domains. They might enable this setting if they prioritize ease of access for users in secondary domains and have additional security measures in place.
- A financial institution with stringent security requirements might keep this setting disabled to ensure that authentication processes for users in any domain are as secure as possible.

**Related Settings:** MixedWindowsPrimaryDomainUseSimpleBinding

**Best Practices:** 

- Configure when: The network security infrastructure sufficiently compensates for the reduced security inherent to simple binding, or when ease of access for secondary domain users is a higher priority.
- Avoid when: The highest level of security is required for authentication, especially in environments where the risk of credential interception or unauthorized access is a critical concern.