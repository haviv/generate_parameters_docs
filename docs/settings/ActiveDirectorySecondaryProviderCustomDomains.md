# Active Directory Secondary Provider Custom Domains

**Technical Name:** ActiveDirectorySecondaryProviderCustomDomains

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The 'Active Directory Secondary Provider Custom Domains' parameter allows administrators to specify custom domains that should be considered when fetching email addresses from a secondary Active Directory source. This parameter is crucial when organizations have multiple Active Directory domains and need to manage user email retrieval across these domains effectively.

**Business Impact:**

Proper configuration of this parameter ensures that user email addresses are accurately retrieved from secondary Active Directory sources when the primary source does not contain the necessary user information. This capability is particularly important in large organizations with complex network topologies and multiple domains. By ensuring accurate email retrieval, organizations can improve their user management processes, enhance security protocols, and maintain compliance with relevant regulations.

**Technical Impact when configured:**

- Enables the system to fetch user email addresses from secondary Active Directory sources using custom domain configurations.
- Ensures accurate user identification and authentication by extending email search capabilities across multiple domains.
- Improves the reliability of user-related workflows and processes by enhancing data accuracy.

**Examples Scenario:**

An organization uses multiple Active Directory domains for different geographical locations. Users from a specific location (e.g., Europe) are unable to log in to certain applications because their email addresses are managed in a secondary AD domain. By setting the 'Active Directory Secondary Provider Custom Domains' parameter, the system can retrieve user email addresses from the specified secondary domain, enabling successful user authentication and access.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** 
- Configure when you manage users across multiple Active Directory domains and require a reliable method to fetch user email addresses from secondary sources.
- Avoid when your organization operates a single Active Directory domain or when there is no need to fetch user data from alternative domains.