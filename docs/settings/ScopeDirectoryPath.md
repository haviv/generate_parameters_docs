**Technical Name:** ScopeDirectoryPath

**Category:** Configuration

**Default Value:** WinNT://{0}/LanmanServer

**Impact Level:** Medium

**Description:**

The `ScopeDirectoryPath` parameter is designed for specifying the path used to scope directory searches within the Pathlock Cloud GRC platform. It is primarily used within connectors that interact with Active Directory to map shared names to directory paths. 

**Business Impact:**

Configuring the `ScopeDirectoryPath` correctly ensures that the Pathlock Cloud GRC platform can accurately and efficiently navigate Active Directory structures to retrieve or update necessary information. This is crucial for maintaining the integrity of user access controls and security policies across the organization.

**Technical Impact when configured:**

When the `ScopeDirectoryPath` is configured, it allows the Pathlock application to properly locate and interact with specific directories in Active Directory. This prevents unnecessary broad searches across the Active Directory, improving performance and reducing potential impacts on Active Directory performance.

**Example Scenario:**

An organization wants to ensure that the Pathlock Cloud GRC platform only interacts with a specific Organizational Unit (OU) in Active Directory to manage security policies for users in that OU. By setting the `ScopeDirectoryPath` to the LDAP path of that OU, the platform will limit its search and management scope to that OU, enhancing security and performance.

**Related Settings:**

- LanmanServerPath

**Best Practices:** 

- Configure `ScopeDirectoryPath` to point directly to the specific directory or OU of interest when interactions with Active Directory should be scoped for efficiency and security.
- Avoid broad or incorrect configurations that may lead to inefficient application behavior or potential security risks due to unintended access to wider directory structures.