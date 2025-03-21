# Additional MS Active Directory domains

**Technical Name:** AdditinalDomains

**Category:** User Management

**Default Value:** None

**Impact Level:** High

**Description:**

The Additional MS Active Directory domains parameter is designed to extend the default domain list by including custom domains that are relevant and recognized within an organization's Active Directory (AD) environment. This facilitates the inclusion and management of users, groups, and other AD objects from these specified domains within the Pathlock Cloud GRC platform.

**Business Impact:**

Incorporating additional domains into the Pathlock system allows for a broader and more flexible management scope over user access and rights across different departments or geographical locations within a multi-domain organization. It enhances security governance by ensuring all relevant domains are under compliance and audit considerations.

**Technical Impact when configured:**

When configured, the system includes the specified domains in its operations, such as user synchronization and authentication processes, enabling a comprehensive Active Directory management that spans across all specified domains. This ensures that users and groups from additional domains are accurately represented and managed within the Pathlock environment.

**Examples Scenario:**

A multinational corporation uses the Pathlock Cloud GRC platform for managing access and security policies across its global operations. The corporation's IT infrastructure includes several Active Directory domains corresponding to different regions and business units. By configuring the `AdditionalDomains` parameter with these domains, the corporation can ensure that its security and compliance policies are uniformly applied and enforced across its entire organizational structure, including all regional offices and subsidiaries.

**Related Settings:**

- `CommonSettings.Default.CustomDomains`
- `CommonSettings.Default.CustomDomainsSplitBy`

**Best Practices:** 

- **Configure when:** You have multiple Active Directory domains that are not part of the default domain but need to be included for comprehensive security and user management.
- **Avoid when:** Your organization operates within a single domain or when all relevant domains are already captured by the default Active Directory settings.